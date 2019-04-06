import argparse
from steg import steg_img
from cryptosteganography import CryptoSteganography
import pyAesCrypt
import os
from os import stat, remove

DEFAULT_ENCRYPTION_PASSWORD = 'Elm34lp9Avm43l2C3n4lkmM1kQwe'

def extract_file(filename, password, outfile):
    extracted_file = CryptoSteganography(password).retrieve(filename)
    with open(outfile + '.aes', 'wb') as encrypted_file:
        encrypted_file.write(extracted_file)

def decrypt_aes(filename, password):
    with open(filename, "rb") as infile:
        with open(filename[:-4], "wb") as outfile:
            try:
                pyAesCrypt.decryptStream(infile, outfile, password, (64 * 1024), stat(filename).st_size)
            except ValueError:
                remove(filename[:-4])

def validate_password(password):
    if password is not None:
        return password
    else:
        return DEFAULT_ENCRYPTION_PASSWORD

def Main():
    parser = argparse.ArgumentParser(description='command-line args')

    parser.add_argument('-f', '--file', help='png image to untangle')
    parser.add_argument('-e', '--extract', help='encrypted file to extract')
    parser.add_argument('-d', '--decrypt', help='encrypted file to decrypt')
    parser.add_argument('-p', '--passwd', help='encryption password')
    
    args = parser.parse_args()
    password = validate_password(args.passwd)

    if args.extract is not None:
        extract_file(args.file, password, args.extract)
    else:
        decrypt_aes(args.decrypt, password)

if __name__ == '__main__':
    Main()
