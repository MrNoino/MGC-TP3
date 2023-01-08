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
        self.__shots = []
        self.__waves = 1
        self.__npc_speed = 1
        self.__score_per_kill = 50
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
        self.serverLog("[SERVER] Servidor ligado, à espera de conexões...")

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

    def send(self, connection, data):

        try:

            data = pickle.dumps(data)

            connection.send(pickle.dumps(data.__sizeof__()))

            connection.send(data)

            return True

        except Exception as e:

            utils.saveLog(EXCEPTIONS_FILENAME, e)

            return False

    def recv(self, connection):

        try:

            dataSize = pickle.loads(connection.recv(16))

            data = pickle.loads(connection.recv(dataSize))

            return data

        except Exception as e:

            utils.saveLog(EXCEPTIONS_FILENAME, e)

            return None

    def generateNPCS(self, INTERVAL):

        self.__npcs = []

        numberNPCS = self.__waves * random.randint(INTERVAL[0], INTERVAL[1])

        numberNPCS = numberNPCS if numberNPCS <= 2000 else 2000

        for i in range(numberNPCS):

            self.__npcs.append({"x": self.__display[0] + (i+1) * random.randint(60, 80), "y": random.randint(80, self.__display[1] -55), "type": ("F" if random.randint(0,1) else "M")})

    def serverLog(self, log):
			
        print(log, '\n')

        utils.saveLog(SERVERLOG_FILENAME, log)


    def setupClient(self, connection):

        data = self.recv(connection)

        name, skin = data 

        currentID = self.__playerID

        self.serverLog("[LOG] "+ "[" + str(currentID) + "] " + name + " se conectou ao servidor.")

        self.send(connection, currentID)

        self.__players[currentID] = {'name': name, "skin": skin, 'x': 50, 'y': random.randint(80, self.__display[1] -55), 'score': 0}

        print(self.__players)

        if len(self.__npcs) == 0:

            self.generateNPCS((2, 5))
            
        data = {"game_info": {"waves": self.__waves, "npc_speed": self.__npc_speed, 'score_per_kill': self.__score_per_kill},"players": self.__players, "npcs": self.__npcs}

        self.send(connection, data)

        self.__waves += 1

        self.__npc_speed *= 1.25

        self.__score_per_kill *= 2

        while True:

            try:

                data = self.recv(connection)

                if not data:
                    break

                data = pickle.loads(data)

                print("[DATA] Recebido do cliente", "[" + str(currentID) + "]", name, ": \"" + str(data) + "\"\n")

                self.generateNPCS((2, 5))

                data = {"game_info": {"waves": self.__waves, "npc_speed": self.__npc_speed, 'score_per_kill': self.__score_per_kill}, "players": self.__players, "npcs": self.__npcs}

                self.send(connection, data)

                print(data)

                self.__waves += 1

                self.__npc_speed *= 1.25

            except WindowsError as e:

                #escreve um log com a exceção
                self.serverLog("[DISCONNECT] [" + str(currentID) + "] " + name + " se desconectou forçadamente.")

                break

            except Exception as e:

                print(e)

                #escreve um log com a exceção
                utils.saveLog(EXCEPTIONS_FILENAME, e)

                break

        self.serverLog("[DISCONNECT]" + " [" + str(currentID) + "] " + name + " se desconectou.")

        self.decrementConnections()

        del self.__players[currentID]
        
        connection.close()



