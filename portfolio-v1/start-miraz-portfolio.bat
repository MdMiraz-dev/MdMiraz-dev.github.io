@echo off
title MIRAZ.DEV - Official Portfolio Server
color 0C
cd /d "%~dp0"

echo ===================================================================
echo               MIRAZ.DEV - OFFICIAL PORTFOLIO SERVER                
echo                  MERAJUL ISLAM (Full-Stack & AI)                   
echo ===================================================================
echo.
echo URL: http://localhost:8080
echo.
echo Server chalu hocche ebong browser auto-open hobe...
echo.
echo [NOTE] Ei black command prompt window-ti bondho korben na.
echo ===================================================================
echo.

start "" http://localhost:8080

node server.js

pause
