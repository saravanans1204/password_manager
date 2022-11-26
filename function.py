from tkinter import END
from tkinter import messagebox
import pyperclip
import json

""" this a just a class which has all the functionality
 related functions in it ass methods"""


class Function:
    def __init__(self, password_text, email_text, website_text) -> None:
        self._password_text = password_text
        self._email_text = email_text
        self._website_text = website_text

    def generate_password(self):
        import string
        import random
        password_text = self._password_text

        password_text.delete(0, END)
        c_alpha = [x for x in string.ascii_uppercase]
        a_alpha = [x for x in string.ascii_lowercase]
        symbol = [x for x in string.punctuation + "$"]

        one = ''.join(random.choices(c_alpha, k=4))
        two = ''.join(random.choices(a_alpha, k=4))
        three = ''.join(random.choices(symbol, k=3))

        password = one + two + three
        password_text.insert(0, password)
        pyperclip.copy(password)

    def save(self):

        website_text = self._website_text
        email_text = self._email_text
        password_text = self._password_text
        website = website_text.get()
        email = email_text.get()
        password = password_text.get()
        new_data = {website: {"email/username": email, "password": password}}

        if len(website) == 0 or len(email) == 0 or len(password) == 0:
            messagebox.showerror(
                title="empty", message="Everything should be filled")
        else:
            is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered : \nEmail:{email}"
                                                                  f"\nPassword :{password} \nIs it ok to save?")

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)

            finally:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
                    website_text.delete(0, END)
                    password_text.delete(0, END)
                    email_text.delete(0, END)

    def search_mail(self):
        website_text = self._website_text

        # try:
        with open("data.json", "r") as data_file:
            read_dic = json.load(data_file)

            # except FileNotFoundError:
            #     with open("data.json","w") as data_file:
            #         pass

            # else:
            #     pass

            def search_inter():
                try:
                    search = website_text.get()
                    s = read_dic[search]

                except KeyError:
                    messagebox.showwarning(
                        title='error', message="the websites credentia"
                                               "ls are not stored in p"
                                               "c \n please add first to search")

                except json.decoder.JSONDecodeError:
                    pass

                else:
                    username = read_dic[search]["email/username"]
                    password = read_dic[search]["password"]
                    ok = messagebox.askyesnocancel(
                        title='credentials', message=f" the username"
                                                     f" :{username}\n the password :"
                                                     f"{password}\n press yes to paste")

                    if ok:
                        self._password_text.delete(0, END)
                        self._email_text.delete(0, END)
                        self._email_text.insert(
                            0, str(read_dic[search]["email/username"]))
                        self._password_text.insert(
                            0, str(read_dic[search]["password"]))

            search_inter()

    def return_commands(self):
        return [self.search_mail, self.generate_password, self.save]
