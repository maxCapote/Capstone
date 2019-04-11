import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = '184.171.144.131'
port = 9999
buf = 1024
addr = (host,port)

file_name='outfile.png'

s.sendto(file_name.encode(),addr)

f=open(file_name,"rb")
data = f.read(buf)
while (data):
    if(s.sendto(data,addr)):
        print("sending ...")
        data = f.read(buf)
s.close()
f.close()
