@echo off
title Launching To Ash Again...
color 0A

:: Step 1: Check for Python
py --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not added to PATH.
    echo 👉 Please install Python from https://www.python.org/downloads/
    pause
    exit /b
)

:: Step 2: Check for Pygame
echo Checking for Pygame...
py -c "import pygame" >nul 2>&1
if errorlevel 1 (
    echo ❗ Pygame not found. Installing it now...
    py -m pip install pygame
    if errorlevel 1 (
        echo ❌ Failed to install Pygame. Please install it manually using:
        echo     py -m pip install pygame
        pause
        exit /b
    )
    echo ✅ Pygame installed successfully.
)

:: Step 3: Run the game using full path from the root folder (no cd)
echo ✅ All systems go. Starting the game...
py files\main.py

pause
