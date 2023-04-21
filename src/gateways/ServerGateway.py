import socket
PORT1 = 8001
PORT2 = 8002
PORT3 = 8003

class ServerGateway:
    def __init__(self):
        self.port1 = 1231
        self.port2 = 1232
        self.port3 = 1233
    
    def connectServer1(self,host="127.0.0.1", port=PORT1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.connect((host, port))
            server.sendto(b"SERVER 1", (host, port))
            server.close()

    def connectServer2(self,host="127.0.0.2", port=PORT2):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.connect((host, port))
            server.sendto(b"SERVER 2", (host, port))
            server.close()

    def connectServer3(self,host="127.0.0.3", port=PORT3):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.connect((host, port))
            server.sendto(b"SERVER 3", (host, port))
            server.close()