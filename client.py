

# import socket
#
#
# class Client:
#     def __init__(self):
#         self.s = socket.socket()
#
#     def response(self):
#         message = self.s.recv(1024)
#         message = message.decode()
#         print("Server Message: ", message)
#         while True:
#             message = self.s.recv(1024)
#             message = message.decode()
#             print("Server: ", message)
#             new_message = input(str("Client: "))
#             new_message = new_message.encode()
#             self.s.send(new_message)
#
#     def check_connection(self):
#         host = input("Enter host name: ")
#         port = int(input("Enter port: "))
#         try:
#             self.s.connect((host, port))
#         except TypeError:
#             print("No connection")
#         else:
#             print("Connected to the server")
#             self.response()
#
#
# client1 = Client()
#
# client1.check_connection()
