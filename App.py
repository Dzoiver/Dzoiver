from tkinter import *
from tkinter import messagebox
import Contacts
import threading
import socket


class App:
    def __init__(self, s, nickname):
        self.s = s
        self.HEIGHT = 640
        self.WIDTH = 640
        self.application_window = Tk()
        self.canvas = Canvas(self.application_window, height=self.HEIGHT, width=self.WIDTH)
        self.chat_frame = Frame(self.application_window, bg="gray")
        self.chat_text = Text(self.chat_frame, state="disabled")
        self.type_frame = Frame(self.application_window, bg="gray")
        self.type_text = Text(self.type_frame)
        # self.info_frame = Frame(self.application_window, bg="gray")
        self.nickname = nickname
        self.type_message = ""
        self.data_type = "message"
        # self.host = "134.209.232.252"
        # self.host = "192.168.0.102"
        # self.port = 9999
        # self.s = socket()
        print("Application initialized")

    def newsocket(self, s):
        self.s = s

    def receive(self):
            while True:
                data = self.s.recv(1024)
                self.chat_text.config(state="normal")
                self.chat_text.insert(INSERT, data)
                self.chat_text.config(state="disabled")

    def setnickname(self):
        pass
        # if len(self.nickname_entry.get()) > 2 and len(self.nickname_entry.get()) < 11:
        #     self.nickname = self.nickname_entry.get()
        #     self.s.send(self.nickname.encode("utf-8")+" ".encode("utf-8")+"zero".encode("utf-8"))
        #     print(self.nickname)
        # else:
        #     print("Invalid nickname")

    def render(self):
        self.canvas.pack()
        self.application_window.title("Dzoiver")

        contacts_frame = Frame(self.application_window, bg="gray")
        contacts_frame.place(relx=0.025, rely=0.025, relwidth=0.3, relheight=0.9)

        # avatar_frame = Frame(self.application_window, bg="gray")
        # avatar_frame.place(relx=0.33, rely=0.025, relwidth=0.25, relheight=0.25)

        # self.info_frame.place(relx=0.6, rely=0.1, relwidth=0.36, relheight=0.175)

        # nickname_label = Label(self.info_frame, text="Enter your nickname", bg="gray")
        # nickname_label.place(relx=0, rely=0.3)
        #
        # nickname_button = Button(self.info_frame, text="Set", command=lambda: self.setnickname())
        # nickname_button.place(relx=0.6, rely=0.5)

        self.chat_frame.place(relx=0.33, rely=0.28, relwidth=0.63, relheight=0.45)

        self.type_frame.place(relx=0.33, rely=0.735, relwidth=0.53, relheight=0.15)

        self.type_text.pack(fill="both")

        send_button = Button(self.application_window, text="Send", command=lambda: self.send_message())
        send_button.place(relx=0.87, rely=0.755, relwidth=0.1, relheight=0.1)

        self.chat_text.pack(fill='both')

        lb1 = Listbox(contacts_frame)
        contacts1 = Contacts.Contacts()
        i = 0
        for contact in contacts1.c_list:
            lb1.insert(i, contact)
            i += 1
        lb1.place(relwidth=0.9, relheight=0.95, relx=0.05, rely=0.03)
        self.application_window.mainloop()

    def add_contacts(self):
        pass

    def send_message(self):
        self.type_message = self.type_text.get(1.0, END)
        try:
            self.s.send("msg".encode('utf-8')
                        + self.nickname.encode('utf-8')
                        + ": ".encode('utf-8')
                        + self.type_message.encode('utf-8'))
        except socket.error:
            print("Can't send because no connection")
            self.type_text.delete(1.0, END)
            self.type_message = ""
            messagebox.showerror("Send error", "Can't send because no connection")
        else:
            self.type_message = ""
            self.chat_text.config(state="normal")
            self.chat_text.insert(INSERT, self.type_message)
            self.chat_text.config(state="disabled")
            self.type_text.delete(1.0, END)

    def run_thread(self):
        receive_thread = threading.Thread(target=self.receive())
        receive_thread.daemon = True
        receive_thread.start()
