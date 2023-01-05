import socket
import pickle
    
host = socket.gethostname()
port = 5555

client_socket = socket.socket()
client_socket.connect((host, port))

message = input("Nome: ")

while message.lower().strip() != 'quit':

    client_socket.send(message.encode())
    data = client_socket.recv(1024)

    players = pickle.loads(data)

    print('Received from server:', players)

    message = input(" -> ")

client_socket.close()