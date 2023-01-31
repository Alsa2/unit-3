# Kivy Homework

## Task 1

### Python code

```py
from kivymd.app import MDApp

class layout_demo(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.original = 0
        self.output = 0


    def build(self):
        return

    def convert_currency(self, choice:str):
        if 'USD' in choice:
                self.output = float("{:.2f}".format(int(self.root.ids.original_in.text)*1.09))
        elif 'JPY' in choice:
            self.output = float("{:.2f}".format(int(self.root.ids.original_in.text)*141))
        else:
            self.output = "Invalid Currency"

        self.root.ids.final_label.text = f"{self.output} {choice}"


demo_class = layout_demo()
demo_class.run()
```
### Kivy code

```kv
Screen:
    size: 500,500
    MDBoxLayout:
        id: main_box
        orientation: 'vertical'
        size_hint:1,.8
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        MDLabel:
            text:"Currency Converter"
            halign: 'center'
            font_style: 'H3'
            text_color: "#000000"
            size_hint: 1, .2
            pos_hint: {'center_x':0.5}

        MDTextField:
            id: original_in
            hint_text: "Enter Amount in EUR:"
            helper_text: "Integers Only"
            helper_text_mode: "on_focus"
            input_filter: 'float'
            pos_hint: {'center_x':0.5}
            size_hint: .7, .1

        MDBoxLayout:
            id: currency_box
            orientation: 'horizontal'
            size_hint: 1, .4
            pos_hint: {'center_x':0.5}
            padding: 10
            spacing: 10
            MDLabel:
                id : hint_label
                text: "Click to convert"
                halign: 'center'
                font_style: 'Overline'
                text_color: "#000000"
                size_hint: .3, 1
                pos_hint: {'center_x':0.2, 'center_y':0.5}
            MDBoxLayout:
                id: button_output_box
                orientation:"vertical"
                size_hint: .3, 1
                MDBoxLayout:
                    id: buttons_box
                    orientation: "horizontal"
                    size_hint: .7, 1
                    pos_hint: {'center_x':0.7, 'center_y':0.9}
                    MDChip:
                        text: "USD"
                        pos_hint: {"center_x": 0.25, "center_y": .25}
                        on_press: app.convert_currency("USD")
                        md_bg_color:"#002B41"
                        text_color: "#FFFFFF"
                    MDChip:
                        text: "JPY"
                        pos_hint: {"center_x": 0.75, "center_y": .25}
                        on_press: app.convert_currency("JPY")
                        md_bg_color:"#F20021"
                MDLabel:
                    id: final_label
                    halign: 'center'
                    font_style: 'H5'
                    text_color: "#000000"
                    size_hint: .3, 1
                    pos_hint: {'center_x':0.6}
                    font_size:80
```

### Proof

![](/Images/kivy-part1-proof.png)

## Task 2

### Python code

```py
from kivymd.app import MDApp
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown


class layout_demo(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.original = 0
        self.output = 0


    def build(self):
        return

    def byte2bit(self):
        self.output = float("{:.2f}".format(int(self.root.ids.byte_in.text)*8))
        self.root.ids.output_label.text = f"{self.output} bits"
    def bit2byte(self):
        self.output = float("{:.2f}".format(int(self.root.ids.bit_in.text)/8))
        self.root.ids.output_label.text = f"{self.output} bytes"

demo_class = layout_demo()
demo_class.run()
```

### Kivy code

```kv
Screen:
    size: 500,500
    MDBoxLayout:
        id: main_box
        orientation: 'vertical'
        size_hint:1,.8
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        MDLabel:
            text: 'Bit/Byte Converter'
            halign: 'center'
            theme_text_color: 'Custom'
            text_color: 0,0,0,1
            font_style: 'H4'
            size_hint: 1, .2
        MDBoxLayout:
            id: byte_box
            orientation: 'horizontal'
            size_hint: 1, .2
            padding: 10
            MDTextField:
                id: byte_in
                hint_text: 'Enter Bytes'
                helper_text: 'Enter Bytes'
                helper_text_mode: 'on_focus'
                input_filter: 'float'
            MDRaisedButton:
                id: byte_button
                text: 'Convert to Bits'
                on_press: app.byte2bit()
        MDBoxLayout:
            id: bit_box
            orientation: 'horizontal'
            size_hint: 1, .2
            padding: 10
            MDTextField:
                id: bit_in
                hint_text: 'Enter Bits'
                helper_text: 'Enter Bits'
                helper_text_mode: 'on_focus'
                input_filter: 'float'
            MDRaisedButton:
                id: bit_button
                text: 'Convert to Bytes'
                on_press: app.bit2byte()

        MDLabel:
            id: output_label
            text: 'Click Convert'
            halign: 'center'
            font_style: 'H4'
            size_hint: 1, .2
```

### Proof

![](/Images/kivy-part2-proof.png)

