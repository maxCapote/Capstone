# Capstone
Code Components  
The final iterations used are stored in the 'Master Final' directory
## Data Extraction Sequence
* Create image file (cover file)
* Encrypt target file (file to be extracted)
* Embed encrypted copy of target file in cover file
* Send copy of cover file with sensitive data to attacker
* Delete both image files and encrypted file
## Data Recovery Sequence
* Extract encrypted file from image file
* Decrypt extracted file
