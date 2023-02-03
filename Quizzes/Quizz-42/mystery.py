from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class mysteryPageA(MDScreen):
    def message1(self):
        print("This is mystery page A you pressed the button")

class mysteryPageB(MDScreen):
    def message2(self):
        print("This is mystery page B you pressed the button")

class layout(MDApp):
    def build(self):
        return
        

mystery = layout()
mystery.run()
