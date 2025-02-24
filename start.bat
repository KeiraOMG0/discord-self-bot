@echo off
setlocal enabledelayedexpansion

:: Hide the console cursor for aesthetics
echo Checking virtual environment...

:: Check if .venv folder exists to skip creation and installation
if not exist ".venv\" (
    echo Creating virtual environment...
    python -m venv .venv
    attrib +h .venv
    echo Installing colorama and discord.py-self from GitHub...
    call .venv\Scripts\activate.bat
    pip install git+https://github.com/dolfies/discord.py-self.git
    pip install colorama
) else (
    echo Virtual environment found. Skipping installation.
)

:: Activate the virtual environment
call .venv\Scripts\activate.bat

:: Run the bot
echo Starting bot...
python main.py

:: Optional: Keep window open if there is an error
if %errorlevel% neq 0 (
    echo An error occurred. Press any key to exit...
    pause
)

endlocal
