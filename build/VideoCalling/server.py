import socket
import threading

# Function to send invitation to all clients
def send_invitation(ip_addresses):
    for client_socket in client_sockets:
        invitation = f"Join video call with IPs: {', '.join(ip_addresses)}"
        client_socket.send(invitation.encode())

# Function to handle client connections
def handle_client(client_socket):
    client_sockets.append(client_socket)
    client_socket.recv(1024)  # Wait for client to be ready
    client_socket.send("Ready to receive invitations".encode())
    while True:
        message = client_socket.recv(1024).decode()
        if message == "start_video":
            ip_addresses = [client[1][0] for client in client_sockets if client[1] != client_socket.getpeername()]
            send_invitation(ip_addresses)
        elif message == "stop_video":
            # Handle video call termination
            pass

# Main function for server
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9999))
    server_socket.listen(5)

    print("Server started. Listening for connections...")

    while True:
        client_socket, _ = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    client_sockets = []
    main()
