from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
import csv

csv_path = "/Users/alsa/Documents/unit-3/Project/Login_kivy/accounts.csv"

class LoginScreen(MDScreen):
    def login(self, username, password):
        
        with open(csv_path, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            
        for row in reader:
            if username == row[0] and password == row[1]:
                self.root.current = "login_success"
                return
            else:
                self.root.ids.error_label.text = "Invalid username or password"



class RegistrationScreen(MDScreen):
    pass

class LoginSuccess(MDScreen):
    pass

class layout(MDApp):
    def build(self):
        return
        

        
    



login = layout()
login.run()