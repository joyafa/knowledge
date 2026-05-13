; 知识库智能问答系统 — NSIS 安装脚本
; 用法: makensis /DVERSION=0.8.17 /DSTAGING_DIR=dist\staging\windows knowledge_setup.nsi

!ifndef VERSION
  !define VERSION "0.8.17"
!endif

!ifndef STAGING_DIR
  !define STAGING_DIR "dist\staging\windows"
!endif

!define APPNAME "KnowledgeAssistant"
!define APPNAME_CN "知识库智能问答系统"

Name "${APPNAME_CN} ${VERSION}"
OutFile "dist\knowledge-setup-${VERSION}-windows.exe"
InstallDir "$PROGRAMFILES64\${APPNAME}"
RequestExecutionLevel admin

; ── 安装向导中的 LLM 配置页面 ──

Page directory
Page custom llmConfigPage llmConfigValidate
Page instfiles

UninstPage uninstConfirm
UninstPage instfiles

; ── 自定义页面变量 ──

Var llmApiBase
Var llmApiKey
Var llmModel

!include "nsDialogs.nsh"
!include "LogicLib.nsh"

Function llmConfigPage
  !insertmacro NSD_CreateText
  nsDialogs::Create 1018
  Pop $0

  ${NSD_CreateLabel} 0 0 100% 12u "配置 LLM API 连接信息（可在安装后通过"编辑配置"修改）"
  Pop $0

  ${NSD_CreateLabel} 0 20u 60u 12u "API 地址:"
  Pop $0
  ${NSD_CreateText} 65u 20u 85% 12u "https://open.bigmodel.cn/api/paas/v4"
  Pop $llmApiBase

  ${NSD_CreateLabel} 0 45u 60u 12u "API 密钥:"
  Pop $0
  ${NSD_CreateText} 65u 45u 85% 12u ""
  Pop $llmApiKey

  ${NSD_CreateLabel} 0 70u 60u 12u "模型名称:"
  Pop $0
  ${NSD_CreateText} 65u 70u 85% 12u "glm-4-flash"
  Pop $llmModel

  nsDialogs::Show
FunctionEnd

Function llmConfigValidate
  ; 无强制校验，用户可安装后再配置
FunctionEnd

; ── 安装段 ──

Section "!${APPNAME_CN}" SEC01
  SetOutPath $INSTDIR

  ; 复制所有文件
  DetailPrint "正在安装文件..."
  File /r "${STAGING_DIR}\*.*"

  ; 创建数据目录
  CreateDirectory "$INSTDIR\data\chroma_db"
  CreateDirectory "$INSTDIR\data\knowledge"
  CreateDirectory "$INSTDIR\data\logs"
  CreateDirectory "$INSTDIR\data\chat_history"

  ; 如果知识库目录为空，复制初始文档
  IfFileExists "$INSTDIR\app\knowledge\*.*" 0 skip_knowledge
  IfFileExists "$INSTDIR\data\knowledge\*.*" skip_knowledge 0
    DetailPrint "正在复制初始知识库文档..."
    CopyFiles "$INSTDIR\app\knowledge\*.*" "$INSTDIR\data\knowledge\"
  skip_knowledge:

  ; 写入 LLM 配置
  DetailPrint "正在写入配置..."
  ${NSD_GetText} $llmApiBase $0
  ${NSD_GetText} $llmApiKey $1
  ${NSD_GetText} $llmModel $2
  ExecWait '"$INSTDIR\python\python.exe" "$INSTDIR\app\scripts\write_config.py" "$INSTDIR\app\config.yaml" "$0" "$1" "$2"'

  ; 修改向量库和知识库路径指向 data 目录
  ExecWait '"$INSTDIR\python\python.exe" -c "import yaml; f=open(r\"$INSTDIR\app\config.yaml\",\"r\",encoding=\"utf-8\"); c=yaml.safe_load(f); f.close(); c[\"vectorstore\"][\"persist_directory\"]=r\"$INSTDIR\data\chroma_db\"; c[\"knowledge\"][\"docs_directory\"]=r\"$INSTDIR\data\knowledge\"; f=open(r\"$INSTDIR\app\config.yaml\",\"w\",encoding=\"utf-8\"); yaml.dump(c,f,default_flow_style=False,allow_unicode=True,sort_keys=False); f.close()"'
SectionEnd

; ── 快捷方式 ──

Section "快捷方式" SEC02
  ; 桌面
  CreateShortCut "$DESKTOP\知识库助手.lnk" "$INSTDIR\launch.bat" "" "$INSTDIR\launch.bat" 0

  ; 开始菜单
  CreateDirectory "$SMPROGRAMS\${APPNAME_CN}"
  CreateShortCut "$SMPROGRAMS\${APPNAME_CN}\启动服务.lnk" "$INSTDIR\launch.bat"
  CreateShortCut "$SMPROGRAMS\${APPNAME_CN}\文档入库.lnk" "$INSTDIR\launch_ingest.bat"
  CreateShortCut "$SMPROGRAMS\${APPNAME_CN}\停止服务.lnk" "$INSTDIR\stop.bat"
  CreateShortCut "$SMPROGRAMS\${APPNAME_CN}\编辑配置.lnk" "$INSTDIR\edit_config.bat"
  CreateShortCut "$SMPROGRAMS\${APPNAME_CN}\打开知识库目录.lnk" "$INSTDIR\open_knowledge.bat"
  CreateShortCut "$SMPROGRAMS\${APPNAME_CN}\卸载.lnk" "$INSTDIR\uninstall.exe"
SectionEnd

; ── 卸载信息 ──

Section -Post
  WriteUninstaller "$INSTDIR\uninstall.exe"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "DisplayName" "${APPNAME_CN}"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "UninstallString" "$INSTDIR\uninstall.exe"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "DisplayVersion" "${VERSION}"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "Publisher" "南昌市星维软件技术中心"
SectionEnd

; ── 卸载段 ──

Section "Uninstall"
  RMDir /r "$INSTDIR"
  Delete "$DESKTOP\知识库助手.lnk"
  RMDir /r "$SMPROGRAMS\${APPNAME_CN}"
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}"
SectionEnd
