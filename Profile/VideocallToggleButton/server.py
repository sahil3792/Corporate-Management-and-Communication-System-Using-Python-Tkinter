from vidstream import StreamingServer

# Start the streaming server
server = StreamingServer('0.0.0.0', 9999)  # Listening on all available network interfaces
server.start_server()