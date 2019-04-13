import App
import netcheck_app
import threading
from socket import *
import network
import time
import tkinter as tk
import Contacts
import account
import userInfo


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
        try:
            time.sleep(1)
            print("Sending data to the server")
            network1.s.send(app1.type_message.encode())
            print("Data is sent")
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
                    time.sleep(2)


def thread3():
    global connected
    time.sleep(1)
    while True:
        try:
            time.sleep(0.5)
            print("Receiving data")
            data = network1.s.recv(1024)
            print("Data is received")
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
            print(data[0:3].decode())
            if data[0:3].decode() == "msg":
                app1.chat_text.config(state="normal")
                app1.chat_text.insert(tk.INSERT, data[3:].decode("utf-8"))
                app1.chat_text.config(state="disabled")
            # if data[0:3].decode() == "nck":
            #     app1.nickname = acc1.name()


network1 = network.Network()
netcheck1 = netcheck_app.Netcheck()
cThread = threading.Thread(target=thread1)
cThread.daemon = True
cThread.start()

netcheck1.render()
user1 = userInfo.Userinfo()

if connection:
    acc1 = account.Account(network1.s)
    acc1.render()
    print("passed acc1 render")
    user1.setnickname(acc1.nickname)
    if acc1.entered:
        contacts = Contacts.Contacts()
        send_thread = threading.Thread(target=thread2)
        send_thread.daemon = True
        send_thread.start()
        receive_thread = threading.Thread(target=thread3)
        receive_thread.daemon = True
        receive_thread.start()
        app1 = App.App(network1.s, user1.nickname)
        app1.render()
network1.close_connection()
