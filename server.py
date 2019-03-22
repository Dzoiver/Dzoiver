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
        time.sleep(3)
        data = c.recv(1024)
        for connection in connections:
            # connection.send(str(a).encode() + " has connected!\n".encode())
            try:
                connection.send(bytes(data))
            except WindowsError:
                print("Connection reseted")
                c.close()
            print(data.decode('utf-8'))
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
