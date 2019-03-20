import socket
import threading


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 9999))
sock.listen(1)
print("Server is started")
connections = []


def handler(c, a):
    while True:
        global connections
        data = c.recv(1024)
        msg = data.decode()
        for connection in connections:
            # connection.send(str(a).encode() + " has connected!\n".encode())
            connection.send(bytes(data))
            print(msg)
        if not data:
            connections.remove(c)
            c.close()
            break


while True:
    print("Waiting for the client...")
    c, a = sock.accept()
    print(a, " has connected!")
    cThread = threading.Thread(target=handler, args=(c, a))
    cThread.daemon = True
    cThread.start()
    connections.append(c)
