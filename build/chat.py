import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkbootstrap import Style
import pymongo
import socket
import threading

# MongoDB setup
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["your_database_name"]  # Update with your database name
users_collection = db["your_collection_name"]  # Update with your collection name

# Server information
SERVER_IP = socket.gethostbyname(socket.gethostname())  # Update with your server's IP address
SERVER_PORT = 5050

# Local user information
LOCAL_IP = socket.gethostbyname(socket.gethostname())  # Get local IP address
LOCAL_PORT = 5051  # Update with the port number you want to use for this client

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_IP, SERVER_PORT))

# Tkinter GUI
def send_message():
    recipient = recipient_var.get()
    message = message_entry.get()
    if recipient and message:
        full_message = f"{recipient}: {message}"
        client_socket.send(full_message.encode())
        message_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please select a recipient and enter a message.")

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            sender, message_content = message.split(":", 1)
            messagebox.showinfo("Message from " + sender, message_content)
        except Exception as e:
            print("Error:", e)
            break

def populate_dropdown():
    usernames = [user["username"] for user in users_collection.find()]
    recipient_var.set("")  # Clear the current selection
    recipient_dropdown['menu'].delete(0, 'end')  # Clear the current options
    for username in usernames:
        recipient_dropdown['menu'].add_command(label=username, command=tk._setit(recipient_var, username))

def start_threads():
    send_thread = threading.Thread(target=send_message)
    send_thread.start()
    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

root = tk.Tk()
root.title("Chat Application")
root.geometry("400x200")

# Create a style
style = Style(theme="darkly")

# Create a frame
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Create labels, entry, combobox, and button
recipient_label = tk.Label(frame, text="Select a recipient:")
recipient_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

recipient_var = tk.StringVar()
recipient_dropdown = ttk.Combobox(frame, textvariable=recipient_var, state="readonly")
recipient_dropdown.grid(row=0, column=1, padx=10, pady=5)

message_label = tk.Label(frame, text="Enter message:")
message_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

message_entry = tk.Entry(frame)
message_entry.grid(row=1, column=1, padx=10, pady=5)

send_button = tk.Button(frame, text="Send", command=start_threads)
send_button.grid(row=2, column=1, padx=10, pady=5)

# Populate the dropdown initially
populate_dropdown()

root.mainloop()

# Close the socket
client_socket.close()
