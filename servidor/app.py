from server import Server
from _thread import *

def main():

	server = Server()

	while True:
		
		if server.getConnections() < 2:

			host, addr = server.getSocket().accept()
			print("[CONNECTION] Conectado a:", addr)

			server.incrementConnections()
			start_new_thread(server.setupClient, (host,))
			server.incrementPlayerID()

	print("[SERVER] Servidor desligado.")

if __name__ == '__main__':
    main()