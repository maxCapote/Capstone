@ECHO OFF
TASKKILL /f /im ra7.exe
DEL "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\klmsdf.bat"
DEL "C:\ProgramData\ra7.exe"
DEL "%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\8uND13.exe"
DEL "%~f0"
