@ECHO OFF
TASKKILL /f /im ra7.exe
DEL "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\klmsdf.exe"
DEL "C:\ProgramData\ra7.exe"
DEL "%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\safeupload.exe"
DEL "%~f0"
