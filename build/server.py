#Personal Message Server
import socket
import threading
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

conn_str = "mongodb+srv://root:812003@cluster0.fshfquh.mongodb.net/?retryWrites=true&w=majority&ssl=true"
client = MongoClient(conn_str, server_api=ServerApi('1'))
AdminDatabase = client["AdminDatabase"]
EmployeeDatabase = client["EmployeeDatabase"]

AdminCollection = AdminDatabase["ManagerCollection"]
EmployeeCollection = EmployeeDatabase["EmployeeCollection"]

# Server configuration
server_ip =  socket.gethostbyname(socket.gethostname())  # Server's local IP address
server_port = 12345  # Port to listen on

EmployeeCollection.update_many({}, { "$set": { "Videoserver_ip": server_ip, "Videoserver_port": server_port } })

def handle_client(client_socket, address):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"Received from {address}: {data}")
            recipient_ip, message = data.split(":")
            broadcast(message, recipient_ip, client_socket)
        except ConnectionAbortedError:
            break

def broadcast(message, recipient_ip, sender_socket):
    for client in clients:
        if clients[client] == recipient_ip:
            try:
                client.send(message.encode('utf-8'))
            except ConnectionResetError:
                continue

def start_server():
    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)
    print("Server is listening...")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        clients[client_socket] = client_address[0]  # Use client's IP address as identifier
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

# Server configuration
server_ip =  socket.gethostbyname(socket.gethostname())  # Server's local IP address
server_port = 12345  # Port to listen on

clients = {}

start_server()
