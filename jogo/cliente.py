import socket
import pickle
import utils

class Network:

    def __init__(self):

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = 5555
        self.addr = (self.host, self.port)

    def connect(self, name, skin):

        self.client.connect(self.addr)
        self.client.send(str.encode(name))        
        self.client.send(str.encode(skin))

        id = self.client.recv()
        return int(id.decode())

    def disconnect(self):

        self.client.close()
    
    def send(self, data, pick = False):

        try:
            if pick:
                self.client.send(pickle.dumps(data))
            else:
                self.client.send(str.encode(data))
            
            reply = self.client.recv()

            try:
                reply = pickle.loads(reply)

            except Exception as e:
                utils.saveLog(e)
            
            return reply
        
        except socket.error as e:
            utils.saveLog(e)