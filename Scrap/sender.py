import subprocess
import argparse

DEFAULT_FILE = "outfile.png"
DEFAULT_USER = "root"
DEFAULT_DESTINATION = "184.171.144.228"
DEFAULT_PATH = "/root/Capstone/GetData"

def validate_options(option, default):
    if option is not None:
        return option
    else:
        return default

def Main():
    parser = argparse.ArgumentParser(description='command-line args')

    parser.add_argument('-f', '--file', help='file to send out')
    parser.add_argument('-u', '--user', help='remote user')
    parser.add_argument('-d', '--destination', help='destination IP address')
    parser.add_argument('-p', '--path', help='destination filepath')
    
    args = parser.parse_args()
    outfile = validate_options(args.file, DEFAULT_FILE)
    user = validate_options(args.user, DEFAULT_USER)
    dst = validate_options(args.destination, DEFAULT_DESTINATION)
    path = validate_options(args.path, DEFAULT_PATH)

    subprocess.Popen(["scp", outfile, user + "@" + dst + ":" + path]).wait()

if __name__ == '__main__':
    Main()
