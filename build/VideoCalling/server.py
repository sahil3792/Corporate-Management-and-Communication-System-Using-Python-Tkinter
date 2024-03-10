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
connected_clients = set()

def handle_client(client_socket, address):
    global invited_user_ipaddresses, connected_clients
    connected_clients.add(address[0])
    try:
        print("invited users ipaddress = ",invited_user_ipaddresses)
        # Receive data from the client
        data = client_socket.recv(1024).decode()
        
        # If the received data is a list of IP addresses
        if data.startswith("IP_ADDRESSES:"):
            # Extract the IP addresses from the data
            ip_addresses = data.split(":")[1].split(",")
            print(ip_addresses)
            
            # Store the IP addresses in the global variable
            invited_user_ipaddresses = ip_addresses
            print(f"Invited users: {invited_user_ipaddresses}")
            for ip_address in invited_user_ipaddresses:
                # Check if the client's IP address is in the list of invited users
                if ip_address in connected_clients:
                    print(f"Notification sent to {ip_address}")
                    send_notification(ip_address)
                else:
                    print(f"{ip_address} is not connected to the server.")
    except Exception as e:
        print(f"Error handling client {address}: {e}")
    finally:
        # Close the client socket
        client_socket.close()

def send_notification(ip_address):
    try:
        document = EmployeeCollection.find_one({'ip_address': ip_address})
        if document:
            # If a document is found, read the corresponding ClientPortNumber value
            client_port = document.get('ClientPortNumber')
            print(f"Client port number for IP address {ip_address}: {client_port}")
            
            # Connect to the client's notification port
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_address = (ip_address, client_port)
            client_socket.connect(server_address)
            
            # Send the notification message
            client_socket.send("Join the meeting".encode())
            client_socket.close()
            
            print(f"Notification sent to {ip_address}")
        else:
            print(f"No document found for IP address {ip_address}")
    except Exception as e:
        print(f"Error sending notification to {ip_address}: {e}")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))  # Bind to the server IP and port
    server_socket.listen(5)

    print("Server started. Listening for connections...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address} established.")
        
        # Handle the client in a separate thread
        client_handler = threading.Thread(target=handle_client, args=(client_socket, address))
        client_handler.start()

# Start the server
start_server()