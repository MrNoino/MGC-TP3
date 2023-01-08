import socket
import pickle
import utils
import time

class Network:

    def __init__(self, host = socket.gethostbyname(socket.gethostname()), port = 5555):

        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__host = host
        self.__port = port
        self.__addr = (self.__host, self.__port)

    def connect(self, name, skin):

        try:

            self.__client.connect(self.__addr)

            reply = self.recv()

            time.sleep(0.5)

            if reply['code'] == 200:

                self.send((name, skin)) 

            return reply

        except Exception as e:

            utils.saveLog(e)

            return None

    def send(self, data):

        try:

            data = pickle.dumps(data)

            self.__client.send(pickle.dumps(data.__sizeof__()))

            time.sleep(0.5)

            self.__client.send(data)
            
            return True
        
        except socket.error as e:

            utils.saveLog(e)

            return False

    def recv(self):

        try:

            dataSize = pickle.loads(self.__client.recv(16))

            time.sleep(0.5)

            data = pickle.loads(self.__client.recv(dataSize))

            return data

        except socket.error as e:

            utils.saveLog(e)

            return None

    def disconnect(self):

        self.__client.close()