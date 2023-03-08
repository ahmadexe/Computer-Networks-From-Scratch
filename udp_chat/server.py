import socket
import threading
import queue

messages = queue.Queue()
clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # DGRAM Tells us its UDP
server.bind(('127.0.0.1', 9999))

def receive():
    while True:
        try:
            message, adrs = server.recvfrom(1024)
            messages.put((message, adrs))
        except: 
            pass
    
    
def broadcast():
    while True:
        while not messages.empty():
            message, adrs = messages.get()
            print(message.decode())
            
            if adrs not in clients:
                clients.append(adrs)
                
            for client in clients:
                try:
                    if message.decode().startsWith("SIGNUP_TAG:"):
                        name = message.decode()[message.decode().index(":") + 1:]
                        server.sendto(f"{name} joined!".encode(), client)
                    
                    else:
                        server.sendto(message, client)
                
                except:
                    clients.remove(client)


t1 = threading.Thread(target=receive)
t2 = threading.Thread(target=broadcast)

t1.start()
t2.start()
