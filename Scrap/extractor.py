from steg import steg_img
from cryptosteganography import CryptoSteganography

def extract_file(filename, password='pass'): # Elm34lp9mvm43l23n4lkmmlkqwe
    crypto_steganography = CryptoSteganography(password)
    decrypted_bin = crypto_steganography.retrieve(filename)
    with open('test.txt.aes', 'wb') as f:
        f.write(decrypted_bin)

def Main():
    filename = input("Image file: ")
    extract_file(filename)

if __name__ == '__main__':
    Main()
