import socket as skt

# Create UDP socket 
udp_socket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)

# Using given address and port 
addr = ("127.0.0.1", 5001)

# Get user message
client_message = input("Enter your name: ")

# Using socket object, the message is sent to UDP server with utf-8 encoding
udp_socket.sendto(client_message.encode('utf-8'), addr)

# recv() method gets message with buffer of 2048 bytes long
message, server = udp_socket.recvfrom(2048)

message = message.decode('utf-8')
print("Answer from server: ", message)

udp_socket.close()