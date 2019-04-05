from PIL import Image
import pyAesCrypt
from steg import steg_img
import os
from cryptosteganography import CryptoSteganography

def create_image():
    img = Image.new('RGB', (1024, 768), (153, 51, 255))
    img.save('cover.png')

def encrypt_file(filename, password='Elm34lp9mvm43'):
    with open(filename, "rb") as infile:
        with open(filename + ".aes", "wb") as outfile:
            pyAesCrypt.encryptStream(infile, outfile, password, (64 * 1024))

def hide_file(embed, cover='cover.png', password='Elm34lp9mvm43'):
    #s = steg_img.IMG(payload_path=embed, image_path=cover)
    #s.hide()
    message = None
    with open(embed, "rb") as f:
        message = f.read()
    crypto_steganography = CryptoSteganography(password)
    crypto_steganography.hide(cover, 'outfile.png', message)

# def send_file():

def delete_unneeded(filename):
    os.remove('cover.png')
    # os.remove('outfile.png')
    os.remove(filename + '.aes')

def Main():
    filename = input("Target file: ")

    create_image()
    encrypt_file(filename)
    hide_file(filename + ".aes")
    delete_unneeded(filename)

if __name__ == '__main__':
    Main()
