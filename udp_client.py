# udp_client.py
import socket

# Set up the client
server_ip = "127.0.0.1"
server_port = 12345
buffer_size = 1024
message = "Hello"

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send message to server
print(f"Client sent the message: \"{message}\"")
client_socket.sendto(message.encode(), (server_ip, server_port))

# Receive response from server
response, _ = client_socket.recvfrom(buffer_size)
print(f"Client received the message: \"{response.decode()}\"")

client_socket.close()
