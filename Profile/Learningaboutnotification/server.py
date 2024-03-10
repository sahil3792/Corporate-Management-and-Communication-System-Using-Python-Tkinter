#Notification Server
import socket
import threading
import pymongo
import subprocess

# List of required packages
required_packages = [
    "ttkbootstrap",
    "pymongo",
    "Pillow",
    "vidstream",
]

# Check if each package is installed, and install it if not
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"Installing {package}...")
        subprocess.check_call(["pip", "install", package])
from pathlib import Path
from tkinter import ttk
from tkinter import *
from ttkbootstrap import Style
import pymongo

from tkinter import filedialog

# Explicit imports to satisfy Flake8

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from vidstream import *
import tkinter as tk
import socket
import threading

import subprocess

try:
    import nltk
    import sklearn
    import pandas
    import docx
except ModuleNotFoundError:
    print("NLTK is not installed. Installing...")
    subprocess.check_call(["pip", "install", "nltk"])
    subprocess.check_call(["pip","install","scikit-learn"])
    subprocess.check_call(["pip","install","pandas"])
    subprocess.check_call(["pip","install","python-docx"])
    import nltk
    import sklearn
    import pandas
    import docx
import tkinter as tk
import socket
import threading
import logging

conn_str = "mongodb+srv://root:812003@cluster0.fshfquh.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(conn_str, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged Your Deplyment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
AdminCollection = None
AdminDatabase = client["AdminDatabase"]
EmployeeDatabase = client["EmployeeDatabase"]
GroupChatDatabase = client["GroupChatDatabase"]

AdminCollection = AdminDatabase["ManagerCollection"]
EmployeeCollection = EmployeeDatabase["EmployeeCollection"]
GroupChatCollection = GroupChatDatabase["GroupChatCollection"]

server_ip =socket.gethostbyname(socket.gethostname())
server_port= 5555

EmployeeCollection.update_many({},{"$set":{"NotificationServerIP": server_ip, "NotificationServerPort": server_port}})

def handle_client(client_socket, clients):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            
            recipients = message.split(":", 1)[0].split(",")
            message_body = message.split(":", 1)[1]
            
            for recipient_ip in recipients:
                recipient_ip = recipient_ip.strip()
                for c in clients:
                    if c["address"][0] == recipient_ip:
                        c["socket"].send(message_body.encode())
                        break
        except Exception as e:
            print("Error:", e)
            break

    # Remove the client from the list once disconnected
    for c in clients:
        if c["socket"] == client_socket:
            clients.remove(c)
            break
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))
    server.listen(5)
    print("Server started, listening on port 5555")

    clients = []
    while True:
        client_socket, _ = server.accept()
        clients.append({"socket": client_socket, "address": client_socket.getpeername()})
        client_handler = threading.Thread(target=handle_client, args=(client_socket, clients))
        client_handler.start()

if __name__ == "__main__":
    start_server()
