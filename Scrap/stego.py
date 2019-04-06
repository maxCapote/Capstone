from steg import steg_img
from cryptosteganography import CryptoSteganography

def hide(embed, cover):
    #s = steg_img.IMG(payload_path=embed, image_path=cover)
    #s.hide()
    message = None
    with open(embed, "rb") as f:
        message = f.read()
    crypto_steganography = CryptoSteganography('My secret password key')
    crypto_steganography.hide(cover, 'outfile.png', message)
    
def reveal(filename):
    #s_prime = steg_img.IMG(image_path=filename)
    #s_prime.extract()
    crypto_steganography = CryptoSteganography('Elm34lp9mvm43')
    decrypted_bin = crypto_steganography.retrieve(filename)
    with open('test.txt.aes', 'wb') as f:
        f.write(decrypted_bin)

def Main():
    """
    embed = input("Embed file: ")
    cover = input("Cover file: ")
    hide(embed, cover)
    """
    filename = input("Fname: ")
    reveal(filename)

if __name__ == '__main__':
    Main()
