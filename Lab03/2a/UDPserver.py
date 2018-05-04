import socket as skt 
from datetime import datetime

# Create UDP socket object 
udp_socket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)

# Tuple containing address and port 
listen_addr = ('127.0.0.1', 5001)

udp_socket.bind(listen_addr)

print("Greetings UDP Server @127.0.0.1:5001")

# Our server application is always running
while True:
    # Getting message from client
    client_message, addr = udp_socket.recvfrom(2048)
    client_message = client_message.decode('utf-8')

    print("Data {} from {}".format(client_message.strip(), addr))

    current_time = int(datetime.now().strftime("%H"))

    # If it's morning
    if (current_time >= 6 and current_time < 12):
        udp_socket.sendto('Bom dia, {}'.format(client_message).encode('utf-8'), addr)

    # Or afternoon
    if (current_time >= 12 and current_time < 18):
        udp_socket.sendto('Boa tarde, {}'.format(client_message).encode('utf-8'), addr)

    # Otherwise, it's night
    if (current_time >= 18 and current_time < 24) or (current_time >= 0 and current_time < 6):
        udp_socket.sendto('Boa noite, {}'.format(client_message).encode('utf-8'), addr)
