@echo off
chcp 65001 >nul
echo 正在打开配置文件...
notepad "%~dp0app\config.yaml"
