@echo off
chcp 65001 >nul
setlocal

set "SCRIPT_DIR=%~dp0"
set "PYTHON=%SCRIPT_DIR%python\python.exe"
set "APP_DIR=%SCRIPT_DIR%app"
set "DATA_DIR=%SCRIPT_DIR%data"
set "MODEL_DIR=%SCRIPT_DIR%model"

:: 设置模型根路径环境变量
set "MODEL_ROOT=%MODEL_DIR%"

echo.
echo ============================================
echo   知识库文档入库工具
echo   扫描 data\knowledge 目录下的文档并入库
echo ============================================
echo.

:: 设置环境变量让 ingest.py 使用 data 目录
set "PYTHONPATH=%APP_DIR%"
cd /d "%APP_DIR%"

"%PYTHON%" scripts\ingest.py

echo.
pause
