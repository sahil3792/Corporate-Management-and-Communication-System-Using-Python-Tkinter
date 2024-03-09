import tkinter as tk
import socket
import threading

class NotificationClient:
    def __init__(self, window):
        self.window = window
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 9999))  # Assuming server is running on localhost and port 9999

        self.lbl_notification = tk.Label(window, text="")
        self.lbl_notification.pack()

    def receive_notification(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                self.lbl_notification.config(text=message)
            except Exception as e:
                print(f"Error receiving notification: {e}")
                break

# Create GUI window
window = tk.Tk()
window.title("Notification Receiver")
window.geometry("300x200")

# Create a client instance
client = NotificationClient(window)

# Start receiving notifications in a separate thread
notification_thread = threading.Thread(target=client.receive_notification)
notification_thread.start()

# Run GUI event loop
window.mainloop()
