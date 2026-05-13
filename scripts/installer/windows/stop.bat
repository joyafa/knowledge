@echo off
chcp 65001 >nul
setlocal

set "SCRIPT_DIR=%~dp0"
set "PID_FILE=%SCRIPT_DIR%data\.pid"

echo 正在停止知识库服务...

:: 优先通过 PID 文件停止
if exist "%PID_FILE%" (
    set /p PID=<"%PID_FILE%"
    taskkill /f /pid !PID! >nul 2>&1
    del "%PID_FILE%" >nul 2>&1
    echo 服务已停止（PID: !PID!）
) else (
    :: 回退：按命令行特征查找 streamlit 进程
    for /f "tokens=2" %%i in ('wmic process where "commandline like '%%streamlit%%app.py%%'" get processid /value 2^>nul ^| findstr /r "[0-9]"') do (
        taskkill /f /pid %%i >nul 2>&1
        echo 服务已停止（PID: %%i）
    )
)

echo.
pause
