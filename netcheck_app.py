from tkinter import *


class Netcheck:
    def __init__(self):
        self.HEIGHT = 100
        self.WIDTH = 220
        self.application_window = Tk()
        self.canvas = Canvas(self.application_window, height=self.HEIGHT, width=self.WIDTH)
        self.label1 = Label(self.application_window, text="Connecting to the server...")
        print("Net check initialized")

    def render(self):
        self.canvas.pack()
        self.application_window.title("Dzoiver")
        self.label1.place(rely=0.4, relx=0.2)
        self.application_window.mainloop()

    def destroy(self):
        self.application_window.destroy()
        print("Netcheck destroyed")
        # self.application_window.destroy()
        # s.send("Closing connection".encode())
        # s.close()

# import socket
# import sys
# from _thread import *
#
# host = ''
# port = 5555
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# try:
#     s.bind((host, port))
# except socket.error as e:
#     print(str(e))
#
# s.listen(5)
# print('Waiting for a connection')
#
# def threaded_client(conn):
#     conn.send(str.encode('Welcome, type your info\n'))
#
#     while True:
#         data = conn.recv(2048)
#         reply = 'Server output: '+data.decode('utf-8')+'\n'
#         if not data:
#             break
#         conn.sendall(str.encode(reply))
#     conn.close()
#
# while True:
#     conn, addr = s.accept()
#     print('connected to: '+addr[0]+':'+str(addr[1]))
#
#     start_new_thread(threaded_client,(conn,))