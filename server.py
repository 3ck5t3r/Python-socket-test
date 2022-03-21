import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 3000))



while True:
    data, addr = server.recvfrom(65535)
    message = b'udp'

    print(data)

    server.sendto(message, addr)