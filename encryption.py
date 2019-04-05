import pyAesCrypt
from os import stat, remove

bufferSize = 64 * 1024

def encrypt(password, filename):
    with open(filename, "rb") as infile:
        with open(filename + ".aes", "wb") as outfile:
            pyAesCrypt.encryptStream(infile, outfile, password, bufferSize)

def decrypt(password, filename):
    with open(filename, "rb") as infile:
        with open(filename[:-4], "wb") as outfile:
            try:
                pyAesCrypt.decryptStream(infile, outfile, password, bufferSize, stat(filename).st_size)
            except ValueError:
                remove(filename[:-4])

def Main():
    filename = input("File to encrypt: ")
    password = input("Password: ")
    encrypt(password, filename)

    """
    filename = input("File to decrypt: ")
    password = input("Password: ")
    decrypt(password, filename)
    """

if __name__ == '__main__':
    Main()
