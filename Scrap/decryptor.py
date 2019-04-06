import pyAesCrypt
import os
from os import stat, remove

def decrypt_aes(filename, password='pass'): # Elm34lp9mvm43l23n4lkmmlkqwe
    with open(filename, "rb") as infile:
        with open(filename[:-4], "wb") as outfile:
            try:
                pyAesCrypt.decryptStream(infile, outfile, password, (64 * 1024), stat(filename).st_size)
            except ValueError:
                remove(filename[:-4])

def Main():
    filename = input("File: ")
    decrypt_aes(filename)

if __name__ == '__main__':
    Main()
