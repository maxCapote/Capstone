"""
    About:

    This is the master program for recovering files that have been received from a client using the bundle
    program. The hidden encrypted file is first extracted from the provided PNG file. Then, the recovered
    file is decrypted.

    Example Usage:

    % python3 unbundle.py -f test.png -e test.txt
    % python3 unbundle.py -f test.png -e test.txt -p password123
"""

import argparse
from cryptosteganography import CryptoSteganography
import pyAesCrypt
from os import stat, remove

DEFAULT_ENCRYPTION_PASSWORD = 'Elm34lp9Avm43l2C3n4lkmM1kQwe'

"""
    The following section contains the primary functions of the program
    ----------------------------------------------------------------------------
"""

def extract_file(filename, extract, password):
    extracted_file = CryptoSteganography(password).retrieve(filename)
    with open(extract + '.aes', 'wb') as encrypted_file:
        encrypted_file.write(extracted_file)

def decrypt_file(filename, password):
    with open(filename, "rb") as infile:
        with open(filename[:-4], "wb") as outfile:
            try:
                pyAesCrypt.decryptStream(infile, outfile, password, (64 * 1024), stat(filename).st_size)
            except ValueError:
                remove(filename[:-4])
    remove(filename)

"""
    The following section contains the secondary/helper functions of the program
    ----------------------------------------------------------------------------
"""

def validate_password(password):
    if password is not None:
        return password
    else:
        return DEFAULT_ENCRYPTION_PASSWORD

"""
    The following section contains the main function of the program
    ----------------------------------------------------------------------------
"""

def Main():
    parser = argparse.ArgumentParser(description='command-line args')

    parser.add_argument('-f', '--file', help='png image to unbundle')
    parser.add_argument('-e', '--extract', help='file to extract')
    parser.add_argument('-p', '--passwd', help='encryption password')

    args = parser.parse_args()
    password = validate_password(args.passwd)

    """
        Summary of process:
        1) Extract encrypted file from PNG
        2) Decrypt the recovered file
    """
    extract_file(args.file, args.extract, password)
    decrypt_file(args.extract + '.aes', password)

if __name__ == '__main__':
    Main()

"""
    ----------------------------------------------------------------------------
"""
