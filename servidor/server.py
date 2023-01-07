import socket
from _thread import *
import pickle
import utils
import random
from globals import *

class Server:

    def __init__(self):

        self.__players = {}
        self.__connections = 0
        self.__playerID = 0

        self.__npcs = []
        self.__waves = 1
        self.__npc_speed = 1
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

    def generateNPCS(self, INTERVAL):

        self.__npcs = []

        numberNPCS = self.__waves * random.randint(INTERVAL[0], INTERVAL[1])

        numberNPCS = numberNPCS if numberNPCS <= 2000 else 2000

        for i in range(numberNPCS):

            self.__npcs.append({"x": self.__display[0] + (i+1) * random.randint(60, 80), "y": random.randint(80, self.__display[1] -55), "type": ("F" if random.randint(0,1) else "M")})

    def setupClient(self, connection):

        data = connection.recv(1024)

        if data:

            name = pickle.loads(data)

        data = connection.recv(1024)

        if data:

            skin = pickle.loads(data)

        currentID = self.__playerID

        print("[LOG]", "[" + str(currentID) + "]", name, " se conectou ao servidor.\n")

        self.__players[currentID] = {'name': name, "skin": skin, "score": 0}

        if len(self.__npcs) == 0:

            self.generateNPCS((2, 5))
            
        data = {"game_info": {"waves": self.__waves, "npc_speed": self.__npc_speed},"players": self.__players, "npcs": self.__npcs}

        data = pickle.dumps(data)

        connection.send(pickle.dumps(data.__sizeof__()))

        connection.send(data)

        self.__waves += 1

        self.__npc_speed *= 1.25

        while True:

            try:

                data = connection.recv(32)

                if not data:
                    break

                data = pickle.loads(data)
                print("[DATA] Recebido do cliente", "[" + str(currentID) + "]", name, ": \"" + str(data) + "\"\n")

                self.generateNPCS((2, 5))

                data = {"game_info": {"waves": self.__waves, "npc_speed": self.__npc_speed},"players": self.__players, "npcs": self.__npcs}

                data = pickle.dumps(data)

                connection.send(pickle.dumps(data.__sizeof__()))

                connection.send(data)

                print(data)

                self.__waves += 1

                self.__npc_speed *= 1.25

            except WindowsError as e:

                #escreve um log com a exceção
                utils.saveLog(EXCEPTIONS_FILENAME, e)

                break

            except Exception as e:

                print(e)

                #escreve um log com a exceção
                utils.saveLog(EXCEPTIONS_FILENAME, e)

                break 


        print("[LOG]", "[" + str(currentID) + "]", name,  "se desconectou.\n")

        self.decrementConnections()

        del self.__players[currentID]
        
        connection.close()



