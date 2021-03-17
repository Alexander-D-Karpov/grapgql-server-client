import socket

sock = socket.socket()
sock.bind(('', 7777))
sock.listen(1)

while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024).decode()
    print(data)
    conn.send('Ok'.encode())
    conn.close()