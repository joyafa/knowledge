@echo off
chcp 65001 >nul
:: 确保知识库目录存在
if not exist "%~dp0data\knowledge" mkdir "%~dp0data\knowledge"
explorer "%~dp0data\knowledge"
