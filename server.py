import socket
import threading
import time
import sqlite3


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.bind(('0.0.0.0', 9999))
except socket.error:
    print("Connection wasn't closed. Restart")
    while True:
        pass

sock.listen(1)
print("Server is started")
connections = []
dataBaseList = []
dbID = 0
pss = ""
nck = ""


def handler(c, a):
    conn = sqlite3.connect('dzoiver.db')
    curs = conn.cursor()
    while True:
        global connections
        global pss
        global nck
        # try:
        #     print("Receiving data")
        #     data = c.recv(1024)
        #     print("Data is received")
        # except socket.error:
        #     print("Receive connection error... closing connection")
        #     connections.remove(c)
        #     c.close()
        #     print("Connection is closed")
        #     break
        # else:
        for connection in connections:
            try:
                data = c.recv(1024)
                        # connection.send(str(a).encode() + " has connected!\n".encode())
                if data[0:3].decode() == "msg":
                    print("Sending data")
                    connection.send(bytes(data))
                    print("Data is sent")
                if data[0:3].decode() == "nck":
                    print("data = " + str(data.decode()))
                    nck = data[3:].decode()
                    data = c.recv(1024)
                    print("data = " + str(data.decode()))
                    pss = data[3:].decode()
                    print("checking if there is exist one")
                    curs.execute("SELECT * FROM users WHERE nickname='{}'".format(nck))
                    fetch = curs.fetchone()
                    print(fetch)
                    if fetch is None:
                        curs.execute("INSERT INTO users (nickname, password) VALUES ('{}', '{}')"
                                                .format(nck, pss))
                        conn.commit()
                        data = "rsl".encode()
                    else:
                        data = "ern".encode()
                    connection.send(data)
                    print(str(data) + "is sent")
                if data[0:3].decode() == "ncq":
                    print("data = " + str(data.decode()))
                    ncq = data[3:].decode()
                    data = c.recv(1024)
                    psq = data[3:].decode()
                    print("ncq = " + ncq)
                    print("psq = " + psq)
                    curs.execute("SELECT * FROM users WHERE nickname='{}' AND password='{}'".format(ncq, psq))
                    fetch = curs.fetchone()
                    print(fetch)
                    if fetch is None:
                        print("No match. Sending error")
                        data = "err".encode()
                    else:
                        print("Match. Sending result")
                        data = "rsl".encode()
                    connection.send(data)
                    print(str(data) + "is sent")
                else:
                    print("???")
            except socket.error:
                print("Send connection error... closing connection")
                connections.remove(c)
                c.close()
                print("Connection is closed")
                break
            print(data[3:].decode('utf-8'))
            if not data:
                print("GGGGGG")
                connections.remove(c)
                c.close()
                break


client_number = 1

while True:
    print("Waiting for the client...")
    c, a = sock.accept()
    print("Client number: " + str(client_number))
    client_number += 1
    print(a, " has connected!")
    cThread = threading.Thread(target=handler, args=(c, a))
    cThread.daemon = True
    cThread.start()
    connections.append(c)

conn.close()
