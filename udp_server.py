# udp_server.py
import socket  # Import the socket library for networking

# Set up the server
server_ip = "127.0.0.1"  # Localhost IP address
server_port = 12345       # Port to listen on
buffer_size = 1024        # Buffer size for receiving data

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a UDP socket
server_socket.bind((server_ip, server_port))  # Bind the socket to the IP and port

print(f"Server is running on {server_ip}:{server_port}")  # Notify that the server is running

while True:
    # Wait to receive a message from a client
    message, client_address = server_socket.recvfrom(buffer_size)
    decoded_message = message.decode()  # Decode the received bytes to string
    print(f"Message received from client: {decoded_message}")  # Print the received message
    
    # Send funny joke
    response = f"{decoded_message} client, why do programmers prefer UDP over TCP? Because they hate handshakes!"
    
    # Send the response back to the client
    server_socket.sendto(response.encode(), client_address)
