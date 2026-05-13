@echo off
chcp 65001 >nul
setlocal

set "SCRIPT_DIR=%~dp0"
set "PYTHON=%SCRIPT_DIR%python\python.exe"
set "APP_DIR=%SCRIPT_DIR%app"
set "DATA_DIR=%SCRIPT_DIR%data"

:: 确保数据目录存在
if not exist "%DATA_DIR%\chroma_db" mkdir "%DATA_DIR%\chroma_db"
if not exist "%DATA_DIR%\knowledge" mkdir "%DATA_DIR%\knowledge"
if not exist "%DATA_DIR%\logs" mkdir "%DATA_DIR%\logs"
if not exist "%DATA_DIR%\chat_history" mkdir "%DATA_DIR%\chat_history"

:: 如果知识库目录为空，从 app/knowledge 复制初始文档
set "KNOWLEDGE_EMPTY=1"
dir /b "%DATA_DIR%\knowledge" >nul 2>&1 && set "KNOWLEDGE_EMPTY=0"
if "%KNOWLEDGE_EMPTY%"=="1" (
    if exist "%APP_DIR%\knowledge" (
        echo 正在复制初始知识库文档...
        xcopy "%APP_DIR%\knowledge\*" "%DATA_DIR%\knowledge\" /s /e /y /q >nul
    )
)

echo.
echo ============================================
echo   知识库智能问答系统
echo   启动后请用浏览器访问: http://localhost:8501
echo   按 Ctrl+C 停止服务
echo ============================================
echo.

"%PYTHON%" -m streamlit run "%APP_DIR%\app.py" ^
  --server.port 8501 ^
  --server.address 0.0.0.0 ^
  --server.headless true ^
  --browser.gatherUsageStats false ^
  --server.enableCORS false

pause
