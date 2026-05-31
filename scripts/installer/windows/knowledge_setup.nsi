; 知识库智能问答系统 — NSIS 安装脚本（PyInstaller 版本）
; 用法: makensis /DVERSION=0.8.17 /DSTAGING_DIR=dist\staging\windows /DOUTDIR=dist knowledge_setup.nsi
;
; 打包 PyInstaller 编译后的 exe，无需内嵌 Python/模型，一键安装。

!ifndef VERSION
  !define VERSION "0.8.17"
!endif

!ifndef STAGING_DIR
  !define STAGING_DIR "dist\staging\windows"
!endif

!ifndef OUTDIR
  !define OUTDIR "dist"
!endif

!define APPNAME "KnowledgeAssistant"
!define APPNAME_CN "知识库智能问答系统"

Name "${APPNAME_CN} ${VERSION}"
OutFile "${OUTDIR}\knowledge-setup-${VERSION}-windows.exe"
InstallDir "$PROGRAMFILES64\${APPNAME}"
RequestExecutionLevel admin

; 非固实压缩：避免 3.6GB staging 超出 NSIS 固实块 2GB 上限
SetCompressor lzma

; ── 安装向导页面 ──

Page directory
Page custom llmConfigPage llmConfigValidate
Page instfiles

UninstPage uninstConfirm
UninstPage instfiles

; ── 变量 ──

Var llmApiBase
Var llmApiKey
Var llmModel

!include "nsDialogs.nsh"
!include "LogicLib.nsh"

; ── LLM 配置页面 ──

Function llmConfigPage
  nsDialogs::Create 1018
  Pop $0

  ${NSD_CreateLabel} 0 0 100% 14u "配置 LLM API 连接信息（可在安装后通过编辑 config.yaml 修改）"
  Pop $0

  ${NSD_CreateLabel} 0 24u 60u 12u "API 地址:"
  Pop $0
  ${NSD_CreateText} 65u 22u 85% 12u "https://open.bigmodel.cn/api/paas/v4"
  Pop $llmApiBase

  ${NSD_CreateLabel} 0 50u 60u 12u "API 密钥:"
  Pop $0
  ${NSD_CreateText} 65u 48u 85% 12u ""
  Pop $llmApiKey

  ${NSD_CreateLabel} 0 76u 60u 12u "模型名称:"
  Pop $0
  ${NSD_CreateText} 65u 74u 85% 12u "glm-4-flash"
  Pop $llmModel

  nsDialogs::Show
FunctionEnd

Function llmConfigValidate
  ; 读取用户输入的 LLM 配置（此时控件仍存在）
  ${NSD_GetText} $llmApiBase $llmApiBase
  ${NSD_GetText} $llmApiKey $llmApiKey
  ${NSD_GetText} $llmModel $llmModel
FunctionEnd

; ── 安装段 ──

Section "!${APPNAME_CN}" SEC01
  SetOutPath $INSTDIR

  ; 复制 PyInstaller 打包的应用目录
  DetailPrint "正在安装文件..."
  File /r "${STAGING_DIR}\*.*"

  ; 创建数据目录
  CreateDirectory "$INSTDIR\data\chroma_db"
  CreateDirectory "$INSTDIR\data\knowledge"
  CreateDirectory "$INSTDIR\data\logs"
  CreateDirectory "$INSTDIR\data\chat_history"
  CreateDirectory "$INSTDIR\model"

  ; 如果知识库数据目录为空，复制初始文档
  IfFileExists "$INSTDIR\knowledge\*.*" 0 skip_knowledge
  IfFileExists "$INSTDIR\data\knowledge\*.*" skip_knowledge 0
    DetailPrint "正在复制初始知识库文档..."
    CopyFiles "$INSTDIR\knowledge\*.*" "$INSTDIR\data\knowledge\"
  skip_knowledge:

  ; 写入 LLM 配置（调用 exe 内置的 --write-config 模式）
  DetailPrint "正在写入 LLM 配置..."
  ExecWait '"$INSTDIR\KnowledgeAssistant.exe" --write-config "$INSTDIR\config.yaml" "$llmApiBase" "$llmApiKey" "$llmModel"'
SectionEnd

; ── 快捷方式 ──

Section "快捷方式" SEC02
  ; 桌面快捷方式
  CreateShortCut "$DESKTOP\知识库助手.lnk" "$INSTDIR\KnowledgeAssistant.exe" "" "$INSTDIR\KnowledgeAssistant.exe" 0

  ; 开始菜单
  CreateDirectory "$SMPROGRAMS\${APPNAME_CN}"
  CreateShortCut "$SMPROGRAMS\${APPNAME_CN}\知识库助手.lnk" "$INSTDIR\KnowledgeAssistant.exe"
  CreateShortCut "$SMPROGRAMS\${APPNAME_CN}\编辑配置.lnk" "notepad.exe" "$INSTDIR\config.yaml"
  CreateShortCut "$SMPROGRAMS\${APPNAME_CN}\数据目录.lnk" "$INSTDIR\data"
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
