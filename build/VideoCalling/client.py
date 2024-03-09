import tkinter as tk
import socket
import threading
# Function to join video call
def join_video_call():
    print("Joining video call")

# Function to send start video call message to server
def start_video_call():
    client_socket.send("start_video".encode())

# Function to send stop video call message to server
def stop_video_call():
    client_socket.send("stop_video".encode())

# Function to handle invitation message
def handle_invitation(invitation):
    print(invitation)
    # Create UI to join video call

# Function to receive invitations from server
def receive_invitations():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 9999))
    client_socket.send("Ready".encode())
    while True:
        invitation = client_socket.recv(1024).decode()
        handle_invitation(invitation)

# Main function for client GUI
def main():
    receive_thread = threading.Thread(target=receive_invitations)
    receive_thread.start()

    window = tk.Tk()
    window.title('Video Conference')
    window.geometry('400x400')

    btn_start_video = tk.Button(window, text="Start Video Call", command=start_video_call)
    btn_start_video.pack()

    btn_stop_video = tk.Button(window, text="Stop Video Call", command=stop_video_call)
    btn_stop_video.pack()

    window.mainloop()

if __name__ == "__main__":
    main()
