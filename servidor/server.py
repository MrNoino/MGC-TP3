import socket
from _thread import *
import pickle
import utils
import random

class Server:

    def __init__(self):

        self.__players = {}
        self.__connections = 0
        self.__playerID = 0

        self.__npcs = []
        self.__waves = 1
        self.__display = (1200, 800)

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

    def getNPCS(self):

        return self.__npcs

    def generateNPCS(self, interval):

        self.__npcs = []

        numberNPCS = self.__waves * random.randint(interval[0], interval[1])

        for i in range(numberNPCS):

            self.__npcs.append({"x": random.randint(self.__display[0] + (i+1) * random.randint(60, 80)), "y": random.randint(80, self.__display[1] -55)})

    def setupClient(self, connection):

        data = connection.recv(16)

        name = data.decode("utf-8")

        currentID = self.__playerID

        print("[LOG]", "[" + str(currentID) + "]", name, " se conectou ao servidor.\n")

        self.__players[currentID] = {'name': name, "score": 0}

        connection.send(pickle.dumps(self.__players))

        while True:

            try:

                data = connection.recv(32)

                if not data:
                    break

                data = data.decode("utf-8")
                print("[DATA] Recebido do cliente", "[" + str(currentID) + "]", name, ": \"" + data + "\"\n")

                self.generateNPCS(2, 5)

                data = {"players": self.__players, "npcs": self.__npcs}

                connection.send(pickle.dumps(data))

                print(data)

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



