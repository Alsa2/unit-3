from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

csv_path = "/Users/alsa/Documents/unit-3/Project/Login_kivy/accounts.csv"

class LoginScreen(MDScreen):
    def login(self, username, password):
        
        with open(csv_path, "r") as file:
            users = file.readlines()

        for user in users:
            if user == f"{username},{password}":
                self.manager.current = "success"
                return
            else:
                self.ids.error_label.text = "Invalid username or password"
                self.ids.password.helper_text_mode = "on_error"
                self.ids.password.helper_text = "Invalid password"
                print("Invalid username or password")



class RegistrationScreen(MDScreen):
    def register(self, username, password, confirm_password):
        if password == confirm_password:
            with open(csv_path, "a") as file:
                file.write(f"{username},{password}\n")
                self.manager.current = "success"
        else:
            self.ids.error_label.text = "Passwords do not match"
            self.ids.password.helper_text_mode = "on_error"
            self.ids.password.helper_text = "Passwords do not match"
            self.ids.confirm_password.helper_text_mode = "on_error"
            self.ids.confirm_password.helper_text = "Passwords do not match"


class LoginSuccess(MDScreen):
    pass

class layout(MDApp):
    def build(self):
        return
        

        
    



login = layout()
login.run()