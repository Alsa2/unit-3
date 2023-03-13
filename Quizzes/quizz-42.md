# Quizz 42
## Python Part
```py
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class MysteryPageA(MDScreen):
    def message1(self):
        print("This is mystery page A you pressed the button")

class MysteryPageB(MDScreen):
    def message2(self):
        print("This is mystery page B you pressed the button")

class layout(MDApp):
    def build(self):
        return
        

mystery = layout()
mystery.run()
```

## KivyMD Part
```kv
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class MysteryPageA(MDScreen):
    def message1(self):
        print("This is mystery page A you pressed the button")

class MysteryPageB(MDScreen):
    def message2(self):
        print("This is mystery page B you pressed the button")

class layout(MDApp):
    def build(self):
        return
        

mystery = layout()
mystery.run()
```
## Proof
![](/Images/quizz42-proof.png)
