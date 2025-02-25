#!/bin/bash

# Hide the console cursor for aesthetics (optional)
echo "Checking virtual environment..."

# Check if .venv folder exists to skip creation and installation
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
    # Hide .venv directory (optional for aesthetics)
    chattr +i .venv
    echo "Installing colorama and discord.py-self from GitHub..."
    source .venv/bin/activate
    pip install git+https://github.com/dolfies/discord.py-self.git
    pip install colorama
else
    echo "Virtual environment found. Skipping installation."
fi

# Activate the virtual environment
source .venv/bin/activate

# Run the bot
echo "Starting bot..."
python3 main.py

# Wait for 2 seconds
sleep 2

# Clear the console (optional)
clear

# Optional: Keep the window open if there is an error
if [ $? -ne 0 ]; then
    echo "An error occurred. Press Enter to exit..."
    read -r
fi
