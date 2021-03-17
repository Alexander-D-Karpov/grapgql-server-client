import socket

sock = socket.socket()
sock.bind(('', 4040))
sock.listen(1)

while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)