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
def handle_client(client_socket, address):
    global invited_user_ipaddresses, connected_clients, notification_ports
    
    # Add the client's IP address to the set of connected clients
    connected_clients.add(address[0])
    
    try:
        # Receive data from the client
        data = client_socket.recv(1024).decode()
        
        # If the received data is a list of IP addresses
        if data.startswith("IP_ADDRESSES:"):
            # Extract the IP addresses from the data and store them
            ip_addresses = set(data.split(":")[1].split(","))
            invited_user_ipaddresses.update(ip_addresses)
            print("Invited users:", invited_user_ipaddresses)
            
            # Send notifications to clients whose IP addresses are in the list
            for ip_address in ip_addresses:
                if ip_address in connected_clients:
                    send_notification(ip_address)
                else:
                    print(f"{ip_address} is not connected to the server.")
    
    except Exception as e:
        print(f"Error handling client {address}: {e}")
    finally:
        # Close the client socket
        client_socket.close()

def send_notification(ip_address):
    global notification_ports
    
    try:
        # Get the notification port for the client
        notification_port = notification_ports.get(ip_address)
        if notification_port is None:
            print(f"No notification port found for {ip_address}")
            return
        
        # Connect to the client's notification port and send the message
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', notification_port))
        client_socket.send("Join the meeting".encode())
        client_socket.close()
        
        print(f"Notification sent to {ip_address}")
    except Exception as e:
        print(f"Error sending notification to {ip_address}: {e}")

def start_server():
    global notification_ports
    
    server_ip = 'localhost'  # Server's IP address
    server_port = 9999  # Port to listen on
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
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