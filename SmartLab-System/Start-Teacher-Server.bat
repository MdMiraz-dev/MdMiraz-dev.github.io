@echo off
title Smart Lab - Teacher Central Controller Server
color 0A
cd /d "%~dp0"

echo =========================================================================
echo       SMART LAB COMMAND CENTER - TEACHER CENTRAL SERVER
echo =========================================================================
echo.
echo [1/2] Starting Central Controller Server on Port 8500...
echo.
echo Your Local Network IP for Student Workstations to connect:
ipconfig | findstr /i "IPv4"
echo.
echo [2/2] Opening Instructor Dashboard in your browser...
start http://localhost:8500
echo.
echo Server is running live! Keep this window open.
echo To stop server, press Ctrl + C.
echo =========================================================================
echo.

python -m uvicorn server.main:app --host 0.0.0.0 --port 8500
pause
