import socket
import threading
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

conn_str = "mongodb+srv://root:812003@cluster0.fshfquh.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(conn_str, server_api=ServerApi('1'))
AdminDatabase = client["AdminDatabase"]
EmployeeDatabase = client["EmployeeDatabase"]

AdminCollection = AdminDatabase["ManagerCollection"]
EmployeeCollection = EmployeeDatabase["EmployeeCollection"]

# Server configuration
server_ip =  socket.gethostbyname(socket.gethostname())  # Server's local IP address
server_port = 9999  # Port to listen on

EmployeeCollection.update_many({}, { "$set": { "Videoserver_ip": server_ip, "Videoserver_port": server_port } })
# Global variable to store invited user IP addresses
invited_user_ipaddresses = []

def handle_client(client_socket, address):
    global invited_user_ipaddresses
    
    # Receive data from the client
    data = client_socket.recv(1024).decode()
    
    # If the received data is a list of IP addresses
    if data.startswith("IP_ADDRESSES:"):
        # Extract the IP addresses from the data
        ip_addresses = data.split(":")[1].split(",")
        
        # Store the IP addresses in the global variable
        invited_user_ipaddresses = ip_addresses
        print(f"Invited users: {invited_user_ipaddresses}")
        
        # Trigger the function on the clients whose IP addresses are in the list
        trigger_notification()

def trigger_notification():
    for ip_address in invited_user_ipaddresses:
        print("below is the ip address that will send notification to")
        print(ip_address)
        print("here in send notification")
        send_notification(ip_address)

def send_notification(ip_address):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (server_ip, 9999)  # Assuming port 8888 for client notifications
        client_socket.connect(server_address)
        client_socket.send("Join the meeting".encode())  # Sending notification message to the client
        client_socket.close()
        print(f"Notification sent to {ip_address}")
    except Exception as e:
        print(f"Error sending notification to {ip_address}: {e}")
    

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))  # Assuming port 9999 for server
    server_socket.listen(5)

    print("Server started. Listening for connections...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address} established.")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, address))
        client_handler.start()

# Start the server
start_server()
