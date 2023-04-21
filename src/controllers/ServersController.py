from src.gateways import ServerGateway
from fastapi import FastAPI

class ServersController:
    def __init__(self, app:FastAPI, serverGateway:ServerGateway.ServerGateway):
        self.app = app
        self.serverGateway = serverGateway
        self.servers = [self.serverGateway.connectServer1, self.serverGateway.connectServer2, self.serverGateway.connectServer3]
    
    def getClient(self, id:int):
        i = 1

        for server in self.servers:
            try:
                server()
                return {"message": f"Connected to server {i}", "clientID": id}
            
            except:
                print(f"Server {i} is down")
            
            i += 1

        return {"message": "All servers are down", "status" : 500}