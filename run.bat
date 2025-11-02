@echo off
REM Verify if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python to continue.
    exit /b 1
)

REM Run the program
python main.py
pause