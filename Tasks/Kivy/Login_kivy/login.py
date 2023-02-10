from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
import sqlite3



class LoginScreen(MDScreen):
    def login(self, username, password):

        username = username.replace("'", "")
        password = password.replace("'", "")
        username = username.replace(";", "")
        password = password.replace(";", "")
        
        conn = sqlite3.connect('Database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        data = c.fetchone()
        if data:
            self.manager.current = "success"
        
        else:
            self.ids.error_label.text = "Invalid username or password"
            self.ids.password.helper_text_mode = "on_error"
            self.ids.password.helper_text = "Invalid password"
            print("Invalid username or password")
        
        conn.close()



class RegistrationScreen(MDScreen):
    def register(self, username, password, confirm_password):
        # prevent sql injection
        username = username.replace("'", "")
        password = password.replace("'", "")
        confirm_password = confirm_password.replace("'", "")
        username = username.replace(";", "")
        password = password.replace(";", "")
        confirm_password = confirm_password.replace(";", "")


        if password == confirm_password:
            conn = sqlite3.connect('Database.db')
            c = conn.cursor()
            c.execute("INSERT INTO users VALUES (NULL, ?, ?, ?)", (username, password, username))
            conn.commit()
            conn.close()
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