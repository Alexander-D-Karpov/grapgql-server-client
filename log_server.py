import socket

sock = socket.socket()
sock.bind(('', 4040))
sock.listen(1)

conn, addr = sock.accept()
print('connected:', addr)
data = conn.recv(1024).decode()
print(data)
conn.send('Ok'.encode())
data = conn.recv(8192)
print(data.decode())
conn.close()