import App
import netcheck_app
import threading
from socket import *
import network
import time
import tkinter as tk


def handler():
    global connection
    try:
        network1.check_connection()
    except:
        netcheck1.label1.config(text="No connection :(")
        print("No connection")
        connection = False
    else:
        netcheck1.label1.config(text="Connected!")
        print("Network established")
        connection = True
        netcheck1.destroy()


def handler2():
    while True:
        time.sleep(3)
        network1.s.send(app1.type_message.encode())


def receive():
        while True:
            time.sleep(1)
            data = network1.s.recv(2048)
            app1.chat_text.config(state="normal")
            app1.chat_text.insert(tk.INSERT, data)
            app1.chat_text.config(state="disabled")


network1 = network.Network()
netcheck1 = netcheck_app.Netcheck()
cThread = threading.Thread(target=handler)
cThread.daemon = True
cThread.start()

netcheck1.render()

if connection:
    send_thread = threading.Thread(target=handler2)
    send_thread.daemon = True
    send_thread.start()
    receive_thread = threading.Thread(target=receive)
    receive_thread.daemon = True
    receive_thread.start()
    app1 = App.App(network1.s)
    app1.render()
network1.close_connection()

#
# def handler(s):
#     global connection
#     time.sleep(3)
#     try:
#         s.connect((host, port))
#     except:
#         netcheck1.label1.config(text="No connection :(")
#         print("No connection")
#         connection = False
#     else:
#         netcheck1.label1.config(text="Connected!")
#         print("Network established")
#         time.sleep(2)
#         connection = True
#
#

# netcheck1.render()
# if connection:
#     app1 = App.App()
#     app1.render()
#
