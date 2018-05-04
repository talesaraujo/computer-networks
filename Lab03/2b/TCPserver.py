import socket as skt 
from datetime import datetime

# Create TCP socket object 
tcp_socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)

# Tuple containing address and port 
listen_addr = ('127.0.0.1', 5002)

tcp_socket.bind(listen_addr)

# Since is a TCP server, the listen waiting operation is required.
tcp_socket.listen()

print("Greetings TCP Server @127.0.0.1:5002")

# Our server application is always running
while True:
    # The requested connection through TCP client is accepted. However, accept() method
    # returns a tuple which contains the address linked to the connection established and 
    # connection_socket is a new instance of Socket class that represents the new information exchange.
    connection_socket, client_address = tcp_socket.accept()


    print("Connected: ", client_address)

    # Getting message from client
    client_message = connection_socket.recv(2048).decode('utf-8')

    print("Client message: {}".format(client_message))

    current_time = int(datetime.now().strftime("%H"))

    # If it's morning
    if (current_time >= 6 and current_time < 12):
        connection_socket.send(('Bom dia, {}'.format(client_message).encode('utf-8')))

    # Or afternoon
    if (current_time >= 12 and current_time < 18):
        connection_socket.send(('Boa tarde, {}'.format(client_message).encode('utf-8')))

    # Otherwise, it's night
    if (current_time >= 18 and current_time < 24) or (current_time >= 0 and current_time < 6):
        connection_socket.send(('Boa noite, {}'.format(client_message).encode('utf-8')))

    connection_socket.close()
    print ("Connection is now finished,{}.".format(client_address))

