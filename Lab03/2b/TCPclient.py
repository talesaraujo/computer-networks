import socket as skt

# Create TCP socket 
tcp_socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)

# Using given address and port 
addr = ("127.0.0.1", 5002)

tcp_socket.connect(addr)

# Get user message
client_message = input("Enter your name: ")

# Using socket object, the message is sent to TCP server with utf-8 encoding
tcp_socket.send(client_message.encode('utf-8'))

# recv() method gets message with buffer of 2048 bytes long
message = tcp_socket.recv(2048).decode('utf-8')

print("Answer from server: ", message)

tcp_socket.close()
