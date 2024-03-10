import socket
import tkinter as tk
from tkinter import messagebox
import threading

SERVER_IP = "192.168.1.109"  # Server IP address
SERVER_PORT = 5555            # Server port number

# Static message template
UserName = "Sahil_shk"
static_message = f"Join the Meeting. You are invited by {UserName}"

def send_notification():
    recipient_ips = entry_ip.get().split(",")
    if not recipient_ips:
        messagebox.showerror("Error", "Please enter recipient IP addresses")
        return

    try:
        for recipient_ip in recipient_ips:
            recipient_ip = recipient_ip.strip()
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((SERVER_IP, SERVER_PORT))
            client_socket.send(f"{recipient_ip}:{static_message}".encode())
            client_socket.close()
        messagebox.showinfo("Success", "Notification sent successfully")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send notification: {e}")

def receive_notifications():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_IP, SERVER_PORT))
        while True:
            message = client_socket.recv(1024).decode()
            if message:
                if message.startswith(static_message):
                    user_invited_by = message.split("by ", 1)[1]
                    print(f"Invited by: {user_invited_by}")
                messagebox.showinfo("Notification", f"Received: {message}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to receive notification: {e}")

# Start receiving notifications in a separate thread
receive_thread = threading.Thread(target=receive_notifications)
receive_thread.start()

root = tk.Tk()
root.title("Notification Client")

label_ip = tk.Label(root, text="Recipient's IP (comma-separated):")
label_ip.grid(row=0, column=0)
entry_ip = tk.Entry(root)
entry_ip.grid(row=0, column=1)

send_button = tk.Button(root, text="Send Notification", command=send_notification)
send_button.grid(row=1, columnspan=2)

root.mainloop()
