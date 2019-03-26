from socket import *


class Network:
    def __init__(self):
        # self.host = "207.154.236.216"
        self.host = "192.168.0.102"
        self.port = 9999
        self.s = socket()
        self.connection_error = False
        print("Network has been setup")

    def check_connection(self):
        print("Connecting")
        self.s.connect((self.host, self.port))
        print("Connected")

    def close_connection(self):
        print("Closing connection")
        self.s.close()
