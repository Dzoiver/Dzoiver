import tkinter
import time


class Account:
    def __init__(self, s):
        self.HEIGHT = 170
        self.WIDTH = 240
        self.s = s
        self.dresult = ""
        self.result = ""
        self.sendInfoList = ["her", "her", "her"]
        self.accountWindow = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.accountWindow,
                                     height=self.HEIGHT,
                                     width=self.WIDTH,)
        self.loginButton = tkinter.Button(self.canvas, text="Log in",
                                     command=lambda: self.login(),
                                          width=12)
        self.enterButton = tkinter.Button(self.accountWindow, text="Enter", command=lambda: self.enter())
        self.nickEntry = tkinter.Entry(self.canvas)
        self.passEntry = tkinter.Entry(self.canvas)
        self.label = tkinter.Label(self.canvas, text="Registration")
        self.errorLabel = tkinter.Label(self.canvas, text="")
        self.mode = 0
        self.success = False
        self.nickname = ""

    @property
    def entered(self):
        return self.success

    @property
    def name(self):
        return self.nickname

    def render(self):
        self.canvas.pack()
        self.loginButton.place(relx=0.6, rely=0.1)
        self.enterButton.place(relx=0.4, rely=0.65)
        self.nickEntry.place(relx=0.2, rely=0.3)
        self.passEntry.place(relx=0.2, rely=0.5)
        self.label.place(relx=0.2, rely=0.1)
        self.errorLabel.place(relx=0.1, rely=0.8)
        self.accountWindow.title("Dzoiver")
        self.accountWindow.mainloop()

    def login(self):
        if self.mode == 0:
            self.label.config(text="Log in")
            self.loginButton.config(text="Registration")
            self.mode = 1
        else:
            self.label.config(text="Registration")
            self.loginButton.config(text="Log in")
            self.mode = 0

    def enter(self):
        self.nickname = self.nickEntry.get()
        if len(self.nickname) < 3 or len(self.nickname) > 15 or len(self.passEntry.get()) < 3 or len(self.passEntry.get()) > 15:
            self.errorLabel.config(text="Incorrect length", fg="red")
        else:
            self.enterButton.config(state='disabled')
            if self.mode == 0:  # registration
                self.s.send("nck".encode() + self.nickEntry.get().encode())
                print("nck is sent")
                self.s.send("pss".encode() + self.passEntry.get().encode())
                print("pss is sent")
            else:  # log in
                self.s.send("ncq".encode() + self.nickEntry.get().encode())
                print("ncq is sent")
                self.s.send("psq".encode() + self.passEntry.get().encode())
                print("psq is sent")
            print("Waiting for answer")
            self.result = self.s.recv(1024)
            print("result is received")
            self.dresult = self.result.decode()
            print("result: " + self.dresult)
            if self.dresult[0:3] == "err":
                self.errorLabel.config(text="Nickname or password is wrong", fg="red")
                print("Error")
                self.enterButton.config(state='normal')
                self.dresult = ""
            elif self.dresult[0:3] == "ern":
                self.errorLabel.config(text="Nickname is already exists", fg="red")
                print("Error")
                self.enterButton.config(state='normal')
                self.dresult = ""
            else:
                self.errorLabel.config(text="Success", fg="green")
                print("goodbye acc1")
                self.success = True
                self.enterButton.config(state='normal')
                self.destroy()

    def destroy(self):
        self.accountWindow.destroy()
