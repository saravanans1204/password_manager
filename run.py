import function
import ui

"""this function just takes the class and runs the app as intented
TO RUN APP YOU CAN JUST CALL run_app FUNCTION"""


def run_app():
    lock = ui.Password_Managers_ui()
    functions = function.Function(
        lock.password_text, lock.email_text, lock.website_text)
    commands = functions.return_commands()
    lock.button_creation(commands=commands)
    lock.window.mainloop()


