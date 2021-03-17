import socket
from server_data import server_ip, server_port

sock = socket.socket()
sock.connect((server_ip, 7777))
sock.send('Ok'.encode())
data = sock.recv(1024).decode()
print(data)
sock.close()