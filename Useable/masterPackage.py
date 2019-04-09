import os
import argparse
import pyAesCrypt
from PIL import Image
from cryptosteganography import CryptoSteganography
import subprocess

DEFAULT_COVER_FILE = 'cover.png'
DEFAULT_OUTFILE = 'outfile.png'
DEFAULT_ENCRYPTION_PASSWORD = 'Elm34lp9Avm43l2C3n4lkmM1kQwe'
DEFAULT_USER = '' # To Be Set to Default Non-Root User
DEFAULT_DESTINATION = '' # Will Change Among Machines
DEFAULT_PATH = '' # /home/default-non-root-user

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

def validate_option(option, default):
    if option is not None:
        return option
    else:
        return default

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

def send_file(outfile, user, dst, path):
    subprocess.Popen(["scp", outfile, user + "@" + dst + ":" + path]).wait()

def clean_up(embed, cover, outfile):
    os.remove(embed + '.aes')
    os.remove(cover)
    os.remove(outfile)

def Main():
    parser = argparse.ArgumentParser(description='command-line args')

    parser.add_argument('-e', '--embed', help='file to embed')
    parser.add_argument('-p', '--password', help='encryption password')
    parser.add_argument('-c', '--cover', help='cover file')
    parser.add_argument('-o', '--outfile', help='output file')
    parser.add_argument('-u', '--user', help='remote user')
    parser.add_argument('-d', '--destination', help='destination IP address')
    parser.add_argument('-fp', '--path', help='destination filepath')
    
    args = parser.parse_args()

    password = validate_option(args.password, DEFAULT_ENCRYPTION_PASSWORD)
    cover = validate_file(args.cover, DEFAULT_COVER_FILE)
    outfile = validate_file(args.outfile, DEFAULT_OUTFILE)
    user = validate_option(args.user, DEFAULT_USER)
    dst = validate_option(args.destination, DEFAULT_DESTINATION)
    path = validate_option(args.path, DEFAULT_PATH)

    if cover == DEFAULT_COVER_FILE:
        create_default_image()
    else:
        create_copy_image(cover)
        cover = cover[:-4] + "_copy" + cover[-4:]

    encrypt_file(args.embed, password)
    hide_file(args.embed + ".aes", cover, outfile, password)
    send_file(outfile, user, dst, path)
    clean_up(args.embed, cover, outfile)

if __name__ == '__main__':
    Main()
