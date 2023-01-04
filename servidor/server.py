import socket
from _thread import *

class Server:

    def __init__(self):

        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server = socket.gethostbyname(socket.gethostname())
        self.__port = 5555

        try:

            self.__socket.bind((self.__server, self.__port))

        except socket.error as e:

            str(e)

            return

        self.__socket.listen(2)
        print("Servidor ligado, à espera de conexões...")


