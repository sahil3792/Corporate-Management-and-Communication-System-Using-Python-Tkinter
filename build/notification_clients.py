import socket
import threading
import tkinter as tk

# Server configuration
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5555

class NotificationClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Notification Client")

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.label = tk.Label(self.frame, text="Messages:")
        self.label.pack()

        self.message_box = tk.Text(self.frame, width=40, height=10)
        self.message_box.pack()

        self.message_entry = tk.Entry(self.frame, width=40)
        self.message_entry.pack()

        self.send_button = tk.Button(self.frame, text="Send", command=self.send_message)
        self.send_button.pack()

        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.start()

    def send_message(self):
        message = self.message_entry.get()
        self.message_box.insert(tk.END, f"You: {message}\n")
        self.message_entry.delete(0, tk.END)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((SERVER_HOST, SERVER_PORT))
            client_socket.send(message.encode('utf-8'))

    def receive_messages(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((SERVER_HOST, SERVER_PORT))
            while True:
                message = client_socket.recv(1024).decode('utf-8')
                self.message_box.insert(tk.END, f"Other: {message}\n")

def main():
    root = tk.Tk()
    app = NotificationClient(root)
    root.mainloop()

if __name__ == "__main__":
    main()
