import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 12345))

file = open('img.jpg', mode="rb")
data = file.read(2048)

while data:
    client.send(data)
    data = file.read(2048)

file.close()
client.close()
