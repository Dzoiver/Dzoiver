import socket
import threading
import time


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 9999))
sock.listen(1)
print("Server is started")
connections = []


def handler(c, a):
    while True:
        global connections
        try:
            data = c.recv(1024)
        except socket.error:
            print("Connection error... closing connection")
            c.close()
        for connection in connections:
            # connection.send(str(a).encode() + " has connected!\n".encode())
            try:
                connection.send(bytes(data))
            except socket.error:
                print("Connection error... closing connection")
                c.close()
            print(data.decode('utf-8'))
        if not data:
            connections.remove(c)
            c.close()
            break
    time.sleep(1)


while True:
    print("Waiting for the client...")
    c, a = sock.accept()
    print(a, " has connected!")
    cThread = threading.Thread(target=handler, args=(c, a))
    cThread.daemon = True
    cThread.start()
    connections.append(c)
