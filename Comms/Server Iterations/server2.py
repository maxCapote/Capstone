# Source: https://stackoverflow.com/questions/13993514/sending-receiving-file-udp-in-python

import socket
import select

host="0.0.0.0"
port = 9999

while True:
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((host,port))
    addr = (host,port)
    buf=1024
    data,addr = s.recvfrom(buf)
    print("Received File:",data.strip())
    f = open(data.strip(),'wb')

    data,addr = s.recvfrom(buf)
    try:
        while(data):
            f.write(data)
            s.settimeout(2)
            data,addr = s.recvfrom(buf)
    except socket.timeout:
        f.close()
        s.close()
        print("File Downloaded")
