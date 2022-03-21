import socket

UDP_MAX_SIZE = 65535

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = b'Hi UDP'

client.sendto(message, ('127.0.0.1', 3000))

data, addr = client.recvfrom(UDP_MAX_SIZE)

client.close()