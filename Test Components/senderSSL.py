import socket
import ssl
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
addr = ('184.171.144.131', 443)
ss.connect(addr)

file = open ("test.txt", "rb")
ss.sendfile(file)
file.close()
resp = ss.recv(1000)
ss.close()
