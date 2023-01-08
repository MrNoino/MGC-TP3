from server import Server
from _thread import *
import pickle
import utils
from globals import *

def main():

	server = Server()

	while True:

		conn, addr = server.getSocket().accept()
		
		if server.getConnections() < 2:

			feedback = pickle.dumps({'code': 200, 'msg': 'Conexão aceite, bem vindo!'})

			conn.send(pickle.dumps(feedback.__sizeof__()))

			conn.send(feedback)

			server.serverLog("[CONNECTION] Conectado a: " + str(addr))

			server.incrementConnections()
			start_new_thread(server.setupClient, (conn,))
			server.incrementPlayerID()

		else:

			feedback = pickle.dumps({'code': 401, 'msg': 'Conexão recusada, limite de jogadores atingidos.'})

			conn.send(pickle.dumps(feedback.__sizeof__()))

			conn.send(feedback)

			conn.close()

	print("[SERVER] Servidor desligado.")

if __name__ == '__main__':
    main()