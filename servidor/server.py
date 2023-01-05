import socket
from _thread import *
import pickle
import utils

class Server:

    def __init__(self):

        self.__players = {}
        self.__connections = 0
        self.__playerID = 0

        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server = socket.gethostbyname(socket.gethostname())
        self.__port = 5555

        try:

            self.__socket.bind((self.__server, self.__port))

        except socket.error as e:

            print(e)

            #escreve um log com a exceção
            utils.saveLog(e)

            return

        self.__socket.listen(2)
        print("[SERVER] Servidor ligado, à espera de conexões...\n")

    def getSocket(self):

        return self.__socket

    def incrementConnections(self):

        self.__connections += 1

    def decrementConnections(self):

        self.__connections -= 1

    def incrementPlayerID(self):

        self.__playerID += 1

    def getConnections(self):

        return self.__connections

    def setupClient(self, connection):

        data = connection.recv(16)

        name = data.decode("utf-8")

        currentID = self.__playerID

        print("[LOG]", "[" + str(currentID) + "]", name, " se conectou ao servidor.\n")

        self.__players[currentID] = {'name': name}

        connection.send(pickle.dumps(self.__players))

        while True:

            try:

                data = connection.recv(32)

                if not data:
                    break

                data = data.decode("utf-8")
                print("[DATA] Recebido do cliente", "[" + str(currentID) + "]", name, ": \"" + data + "\"\n")

                connection.send(pickle.dumps(self.__players))

            except WindowsError as e:

                #escreve um log com a exceção
                utils.saveLog(e)

                break

            except Exception as e:

                print(e)

                #escreve um log com a exceção
                utils.saveLog(e)

                break 


        print("[LOG]", "[" + str(currentID) + "]", name,  "se desconectou.\n")

        self.decrementConnections()

        del self.__players[currentID]
        
        connection.close()



