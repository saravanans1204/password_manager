from tkinter import *

from configs import BG_COLOR


import json

""" this a just a class which is responsible for building the gui """


class Password_Managers_ui():
    def __init__(self) -> None:
        # gui creation
        self.window = Tk()
        self.window.resizable(width=False, height=False)
        self.window.config(bg=BG_COLOR, padx=100, pady=100)
        self.window.title("saravanan password manager")
        self.lock_img = PhotoImage(file='./image/lock.png')
        self.lock_canvas = Canvas(width=200, height=200, highlightthickness=0)
        self.lock_canvas.create_image(100, 100, image=self.lock_img)
        self.lock_canvas.config(bg=BG_COLOR)
        self.lock_canvas.grid(column=1, row=0)
        self.title = Label(text="Password Manager", font=(
            'Ubuntu', 20, 'bold'), bg=BG_COLOR)
        self.title.grid(column=1, row=0)

        self.website_text = Label(
            text="Website:", font=('Ubuntu', 14), bg=BG_COLOR)
        self.website_text.grid(column=0, row=1)

        self.email = Label(text="Email/Username:",
                           font=('Ubuntu', 14), bg=BG_COLOR)
        self.email.grid(column=0, row=2)

        self.password = Label(
            text="password:", font=('Ubuntu', 14), bg=BG_COLOR)
        self.password.grid(column=0, row=3)

        self.website_text = Entry(width=41)
        self.website_text.grid(column=1, row=1)

        self.email_text = Entry(width=59)
        self.email_text.grid(column=1, row=2, columnspan=2)

        self.password_text = Entry(width=41)
        self.password_text.grid(column=1, row=3)
        self._json_file_creater()

    # Buttons_____________________________________

    def button_creation(self, commands):

        self.search_button = Button(text="search", width=14,
                                    borderwidth=0, height=0, command=commands[0])
        self.search_button.grid(column=2, row=1)

        self.generate_password = Button(text="Generate password", width=14,
                                        borderwidth=0, height=0, command=commands[1])
        self.generate_password.grid(column=2, row=3)

        self.add_button = Button(text="Add", width=50, command=commands[2])
        self.add_button.grid(row=4, column=1, columnspan=2, pady=10)

    def _json_file_creater(self):
        with open("data.json", "w") as data_file:
            json.dump({}, data_file)
            print(data_file)
