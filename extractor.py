from steg import steg_img

def extract_file(filename):
    s_prime = steg_img.IMG(image_path=filename)
    s_prime.extract()

def Main():
    filename = input("Image file: ")
    extract_file(filename)

if __name__ == '__main__':
    Main()
