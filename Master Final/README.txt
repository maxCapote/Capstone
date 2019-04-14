To Note:

0) DO NOT extract the 7z file
   - It contains the Word doc with a malicious macro, which will trip
     antivirus on your computer (assuming you use a decent enough AV)

1) The Python files for data exfiltration and recovery are fully commented

2) Of the BATCH files, only klmsdf.bat is commented
    - safescan.bat is delivered to the victim as is, so we would not want
      to deliver a documented file for the user to find and audit

3) The file klmsdf.exe corresponds to klmsdf.bat and safeupload.exe
   corresponds to bundle.py
