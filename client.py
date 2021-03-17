import socket

sock = socket.socket()
sock.connect((server_ip, 4040))

sock.close()