import socket
import threading

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
