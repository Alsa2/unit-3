# Quizz 40

## Code:
    
### Kivy:
``` KIVY
Screen:
    size: 500, 500

    MDCard:
        orientation: 'vertical'
        size_hint: .7, .3
        pos_hint: {'center_x': .5, 'center_y': .5}
        md_bg_color: "#FFFF00"

        MDBoxLayout:
            id: main_box
            orientation: 'vertical'
            size_hint: .7, .3
            pos_hint: {'center_x': .5, 'center_y': .5}
            mb_bg_color: "#00FF00"

            MDLabel:
                id: counter_label
                font_style: 'H3'
                text: '0'
                pos_hint: {'center_x': .5, 'center_y': .5}

            MDRaisedButton:
                id: plus_button
                text: '+1'
                #stick to the right
                pos_hint: {'center_x': .5, 'center_y': .5}
                size_hint: .5, .5
                on_release: app.change()
```
### Python:
``` python
from kivymd.app import MDApp

class layout_demo(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.count = 0

    def build(self):
        return

    def change(self):
        self.count += 1
        self.root.ids.counter_label.text = f"x= {self.count}"



demo_class = layout_demo()
demo_class.run()
    
```
## Proof:

![](/Images/quizz39-proof.png)