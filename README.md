### Distributed System with Server Redundancy Using Socket and FastAPI API

This is a project that implements a distributed system using the socket message passing technique, where a server is responsible for handling requests and, if it goes offline, the next available server takes over. A client/server API was created using the FastAPI framework to facilitate the consumption of services offered by the system.

#### How to run

To run the project, follow these instructions:

1. Install all dependencies using the command below:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute all servers by opening the "servers" folder and running the commands below in separate terminals:
   ```bash
   python3 server1.py
   ```
   ```bash
   python3 server2.py
   ```
   ```bash
   python3 server3.py
   ```
3. Run the API. In the project root folder, execute the command below in a separate terminal:
   ```bash
   python3 -m uvicorn src.main:app --reload
   ```
4. Make requests using an HTTP client (such as Insomnia, for example) to consume the services offered by the system.