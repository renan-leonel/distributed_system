from src.controllers import ServersController
from src.gateways import ServerGateway
from fastapi import FastAPI

app = FastAPI()
serverGateway = ServerGateway.ServerGateway()
serversController = ServersController.ServersController(app, serverGateway)

@app.get("/tcp")
async def getClientTcp(id:int):
    returnMessage = serversController.getClient(id)
    return returnMessage