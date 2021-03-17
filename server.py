import socket
from python_graphql_client import GraphqlClient
from server_data import endpoint
from log_server_data import *


sock = socket.socket()
sock.bind(('', 7777))
sock.listen(1)

while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024).decode()
    print(data)
    conn.send('Ok'.encode())
    id = conn.recv(1024)
    conn.close()

def graphql_con(id):
    client = GraphqlClient(endpoint)
    query = """
    query countryQuery($user_data: String) {
        user_data(id:$id) {
            id
            name
            role
        }
    }
    """
    variables = {"id": id}

    data = client.execute(query=query, variables=variables)
    print(data)

def logserv_con(inf):
    sock = socket.socket()
    sock.connect((server_ip, server_port))
    sock.send('Ok'.encode())
    data = sock.recv(1024).decode()
    print(data)
    sock.send(inf)
    sock.close()
