# Quizz 40

## Code:
    
### Kivy:
``` KIVY
MDScreen:
    size:500,500
    MDBoxLayout:
        id: main_screen
        orientation:"vertical"
        md_bg_color: "#FFFFFF"

        MDLabel:
            id:name
            text: "Alex"
            halign: "center"
            font_style: "H1"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            pos_hint: {"center_x": .5, "center_y": .5}

        MDRaisedButton:
            id: changebutton
            text: "Dark Mode"
            pos_hint: {"center_x": 0.06, "center_y": 0.1}
            on_release: app.change_theme()
```
### Python:
``` python
from kivymd.app import MDApp

class layout_demo(MDApp):
    def build(self):
        return
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color_positive = "black"
        self.color_negative = "white"

    def change_theme(self):
        if self.color_positive == "black":
            self.color_positive = "white"
            self.root.ids.main_screen.md_bg_color = "#000000"
            self.root.ids.changebutton.text_color = 1,1,1,1
            self.root.ids.name.text_color = 1, 1, 1, 1
            self.root.ids.changebutton.text = "Light Mode"


        else:
            self.color_positive = "black"
            self.root.ids.main_screen.md_bg_color = "#FFFFFF"
            self.root.ids.changebutton.text_color = 0,0,0,1
            self.root.ids.name.text_color = 0, 0, 0, 1
            self.root.ids.changebutton.text = "Dark Mode"



demo_class = layout_demo()
demo_class.run()
```
## Proof:

![](/Images/quizz40-proof.png)