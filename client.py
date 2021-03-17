import socket
from server_data import *

def sock_con(id):
    sock = socket.socket()
    sock.connect((server_ip, server_port))
    sock.send('Ok'.encode())
    data = sock.recv(1024).decode()
    print(data)
    sock.send(id)
    sock.close()

sock_con(69420)