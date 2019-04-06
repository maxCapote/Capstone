import os
import sys
import argparse
import requests
import pyAesCrypt
from PIL import Image
from cryptosteganography import CryptoSteganography

DEFAULT_COVER_FILE = 'cover.png'
DEFAULT_OUTFILE = 'outfile.png'
DEFAULT_ENCRYPTION_PASSWORD= 'Elm34lp9Avm43l2C3n4lkmM1kQwe'

def create_default_image():
    img = Image.new('RGB', (4096, 3072), (153, 51, 255))
    img.save(DEFAULT_COVER_FILE, "PNG")

def create_copy_image(cover):
    try: 
        img = Image.open(cover)
        img.save(cover[:-4] + "_copy" + cover[-4:])
    except IOError: 
        pass

def encrypt_file(embed, password):
    with open(embed, "rb") as infile:
        with open(embed + ".aes", "wb") as outfile:
            pyAesCrypt.encryptStream(infile, outfile, password, (64 * 1024))

def hide_file(embed, cover, outfile, password):
    data = None
    with open(embed, "rb") as infile:
        data = infile.read()
    CryptoSteganography(password).hide(cover, DEFAULT_OUTFILE, data)
    check_file_rename(DEFAULT_OUTFILE, outfile)

def validate_password(password):
    if password is not None:
        return password
    else:
        return DEFAULT_ENCRYPTION_PASSWORD

def validate_file(filename, default):
    if (filename is not None) and (check_file_extension(filename)):
        return filename
    else:
        return default

def check_file_extension(filename):
    if (filename[-4:] == '.png') or (filename[-4:] == '.PNG'):
        return True
    else:
        return False

def check_file_rename(current_name, new_name):
    if new_name != DEFAULT_OUTFILE:
        os.rename(current_name, new_name)

def send_file(outfile):
    print("Coming")

def clean_up(embed, cover, outfile):
    os.remove(embed + '.aes')
    os.remove(cover)
    os.remove(outfile)

def Main():
    parser = argparse.ArgumentParser(description='command-line args')

    parser.add_argument('-e', '--embed', help='file to embed')
    parser.add_argument('-p', '--passwd', help='encryption password')
    parser.add_argument('-c', '--cover', help='cover file')
    parser.add_argument('-o', '--outfile', help='output file')
    
    args = parser.parse_args()

    password = validate_password(args.passwd)
    cover = validate_file(args.cover, DEFAULT_COVER_FILE)
    outfile = validate_file(args.outfile, DEFAULT_OUTFILE)

    if cover == DEFAULT_COVER_FILE:
        create_default_image()
    else:
        create_copy_image(cover)
        cover = cover[:-4] + "_copy" + cover[-4:]

    encrypt_file(args.embed, password)
    hide_file(args.embed + ".aes", cover, outfile, password)
    send_file(outfile)
    clean_up(args.embed, cover, outfile)

if __name__ == '__main__':
    Main()
