import tkinter as tk
from tkinter import messagebox
import Contacts


class App:
    def __init__(self):
        self.HEIGHT = 640
        self.WIDTH = 640
        self.application_window = tk.Tk()
        self.entry = tk.Entry()

    def render(self):
        canvas = tk.Canvas(self.application_window, height=self.HEIGHT, width=self.WIDTH)
        canvas.pack()
        self.application_window.title("Dzoiver")

        contacts_frame = tk.Frame(self.application_window, bg="gray")
        contacts_frame.place(relx=0.025, rely=0.025, relwidth=0.3, relheight=0.9)

        avatar_frame = tk.Frame(self.application_window, bg="gray")
        avatar_frame.place(relx=0.33, rely=0.025, relwidth=0.25, relheight=0.25)

        info_frame = tk.Frame(self.application_window, bg="gray")
        info_frame.place(relx=0.6, rely=0.1, relwidth=0.36, relheight=0.175)

        chat_frame = tk.Frame(self.application_window, bg="gray")
        chat_frame.place(relx=0.33, rely=0.28, relwidth=0.63, relheight=0.45)

        type_frame = tk.Frame(self.application_window, bg="gray")
        type_frame.place(relx=0.33, rely=0.735, relwidth=0.63, relheight=0.15)

        lb1 = tk.Listbox(contacts_frame)
        contacts1 = Contacts.Contacts()
        i = 0
        for contact in contacts1.c_list:
            lb1.insert(i, contact)
            i += 1
        lb1.place(relwidth=0.9, relheight=0.95, relx=0.05, rely=0.03)
        self.application_window.mainloop()
