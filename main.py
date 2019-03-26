import App
import netcheck_app
import threading
from socket import *
import network
import time
import tkinter as tk


def thread1():
    global connection, connected
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
        connected = True
        netcheck1.destroy()


def thread2():
    global connected
    while True:
        time.sleep(2)
        try:
            network1.s.send(app1.type_message.encode())
        except error:
            connected = False
            network1.s = socket()
            print("connection in send lost... reconnecting")
            while not connected:
                try:
                    network1.check_connection()
                    connected = True
                    print("re-connection in send successful")
                    app1.newsocket(network1.s)
                except error:
                    print("snn hotel")
                    time.sleep(2)


def thread3():
    global connected
    while True:
        time.sleep(1)
        try:
            data = network1.s.recv(1024)
        except error:
            connected = False
            network1.s = socket()
            print("connection in recv lost... reconnecting")
            while not connected:
                try:
                    if not connected:
                        network1.check_connection()
                        connected = True
                        print("re-connection in recv successful")
                        app1.newsocket(network1.s)
                except error:
                    time.sleep(2)
        else:
            app1.chat_text.config(state="normal")
            app1.chat_text.insert(tk.INSERT, data)
            app1.chat_text.config(state="disabled")


network1 = network.Network()
netcheck1 = netcheck_app.Netcheck()
cThread = threading.Thread(target=thread1)
cThread.daemon = True
cThread.start()

netcheck1.render()

if connection:
    send_thread = threading.Thread(target=thread2)
    send_thread.daemon = True
    send_thread.start()
    receive_thread = threading.Thread(target=thread3)
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
