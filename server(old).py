import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 12345))
server.listen()

client_socket, client_address = server.accept()

file = open('img_server.jpg', mode="wb")
data = client_socket.recv(2048)

while data:
    file.write(data)
    date = client_socket.recv(2048)

file.close()
