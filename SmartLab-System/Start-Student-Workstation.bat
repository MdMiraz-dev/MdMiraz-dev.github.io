@echo off
title Smart Lab - Student Workstation Agent
color 0B
cd /d "%~dp0"

echo =========================================================================
echo       SMART LAB COMMAND CENTER - STUDENT WORKSTATION AGENT
echo =========================================================================
echo.
set /p TEACHER_IP="Enter Teacher PC IP Address (Press Enter for localhost / this PC): "
if "%TEACHER_IP%"=="" set TEACHER_IP=127.0.0.1

set /p PC_ID="Enter Workstation ID (e.g. LAB-PC-01, press Enter for LAB-PC-01): "
if "%PC_ID%"=="" set PC_ID=LAB-PC-01

set /p S_NAME="Enter Student Name (press Enter for Student 1): "
if "%S_NAME%"=="" set S_NAME=Student 1

echo.
echo Connecting to Teacher Server at %TEACHER_IP%:8500...
echo Workstation: %PC_ID% (%S_NAME%)
echo.
echo Streaming live telemetry, screen captures, and listening for lock commands...
echo Keep this window running in background.
echo =========================================================================
echo.

python -m agent.client_agent --host %TEACHER_IP% --port 8500 --client-id %PC_ID% --student "%S_NAME%"
pause
