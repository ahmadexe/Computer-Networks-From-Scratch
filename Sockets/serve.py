import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 44444))
s.listen()

while True:
    client, address = s.accept()
    print("Connected to: {}".format(str(address)))
    client.send("You're connected".encode())
    client.close()
          
