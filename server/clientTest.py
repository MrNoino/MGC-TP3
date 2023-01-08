import socket
import pickle
    
host = socket.gethostname()
port = 5555

client_socket = socket.socket()
client_socket.connect((host, port))

name = input("Nome: ")

skin = input("Skin: ")

if name.lower().strip() != 'quit':

    client_socket.send(pickle.dumps(name))

else:

    exit()

if skin.lower().strip() != 'quit':

    client_socket.send(pickle.dumps(skin))

else:

    exit()

sizeData = client_socket.recv(16)

sizeData = pickle.loads(sizeData)

data = client_socket.recv(sizeData)

data = pickle.loads(data)

print('Received from server:', data)

while True:

    client_socket.send(pickle.dumps({'x': 12, "y": 12}))

    sizeData = client_socket.recv(16)

    sizeData = pickle.loads(sizeData)

    data = client_socket.recv(sizeData)

    data = pickle.loads(data)

    print('Received from server:', data)

    print(len(data["npcs"]))

client_socket.close()