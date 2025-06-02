@echo off
setlocal

REM === CONFIG ===
set GAME_NAME=ToAshAgain
set FINAL_FOLDER=%USERPROFILE%\Desktop\To Ash Again
set SOURCE_FOLDER=%USERPROFILE%\Desktop\%GAME_NAME%
set ICON_FILE=%SOURCE_FOLDER%\icon.ico

REM === CLEANUP OLD FINAL FOLDER IF EXISTS ===
if exist "%FINAL_FOLDER%" (
    rmdir /s /q "%FINAL_FOLDER%"
)
mkdir "%FINAL_FOLDER%"

REM === RUN PYINSTALLER FROM INSIDE FILES FOLDER ===
cd /d "%SOURCE_FOLDER%\files"
pyinstaller --noconfirm --windowed ^
 --name "To Ash Again" ^
 --distpath "%FINAL_FOLDER%" ^
 --workpath "%SOURCE_FOLDER%\temp_build" ^
 --specpath "%SOURCE_FOLDER%\temp_build" ^
 --icon "%ICON_FILE%" main.py

REM === COPY ASSETS INTO FINAL FOLDER ===
xcopy "%SOURCE_FOLDER%\assets" "%FINAL_FOLDER%\assets" /E /I /Y >nul

REM === MOVE EXECUTABLE & _internal OUT OF INNER FOLDER ===
move "%FINAL_FOLDER%\ToAshAgain\To Ash Again.exe" "%FINAL_FOLDER%\" >nul
move "%FINAL_FOLDER%\ToAshAgain\_internal" "%FINAL_FOLDER%\" >nul

REM === DELETE INNER BUILD FOLDER ===
rmdir /s /q "%FINAL_FOLDER%\ToAshAgain"

REM === CLEANUP ===
rmdir /s /q "%SOURCE_FOLDER%\build"
rmdir /s /q "%SOURCE_FOLDER%\dist"
rmdir /s /q "%SOURCE_FOLDER%\temp_build"
del "%SOURCE_FOLDER%\ToAshAgain.spec"

echo ===============================
echo ✅ Done! Open: "%FINAL_FOLDER%"
echo ===============================
pause
