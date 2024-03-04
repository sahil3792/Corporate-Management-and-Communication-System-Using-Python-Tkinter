import socket
import threading
import tkinter as tk

def receive_messages():
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            message_listbox.insert(tk.END, data)
        except ConnectionAbortedError:
            break

def send_message(event=None):
    message = my_message.get()
    if message:
        recipient_ip = recipient_ip_entry.get()
        full_message = f"{recipient_ip}:{message}"
        client_socket.send(full_message.encode('utf-8'))
        message_listbox.insert(tk.END, "You: " + message)
        my_message.set("")

def connect_to_server():
    global client_socket
    global receive_thread
    server_ip = server_ip_entry.get()
    server_port = int(server_port_entry.get())
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

# GUI setup
root = tk.Tk()
root.title("Chat Application")

message_listbox = tk.Listbox(root, width=50, height=20)
message_listbox.pack(pady=10)

my_message = tk.StringVar()
message_entry = tk.Entry(root, textvariable=my_message)
message_entry.pack(pady=5)
message_entry.bind("<Return>", send_message)

recipient_ip_label = tk.Label(root, text="Recipient IP:")
recipient_ip_label.pack()
recipient_ip_entry = tk.Entry(root)
recipient_ip_entry.pack()

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

server_ip_label = tk.Label(root, text="Server IP:")
server_ip_label.pack()
server_ip_entry = tk.Entry(root)
server_ip_entry.pack()

server_port_label = tk.Label(root, text="Server Port:")
server_port_label.pack()
server_port_entry = tk.Entry(root)
server_port_entry.pack()

connect_button = tk.Button(root, text="Connect", command=connect_to_server)
connect_button.pack(pady=5)

root.mainloop()
