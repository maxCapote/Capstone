from steg import steg_img

def hide(embed, cover):
    s = steg_img.IMG(payload_path=embed, image_path=cover)
    s.hide()

def reveal(filename):
    s_prime = steg_img.IMG(image_path=filename)
    s_prime.extract()

def Main():
    embed = input("Embed file: ")
    cover = input("Cover file: ")
    hide(embed, cover)
    """
    filename = input("Fname: ")
    reveal(filename)
    """

if __name__ == '__main__':
    Main()
