from kivymd.app import MDApp

class layout_demo(MDApp):
    def build(self):
        return
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color_positive = "black"
        self.color_negative = "white"

    def change_color(self):
        if self.color_positive == "black":
            self.color_positive = "white"
            self.color_negative = "black"
            self.root.ids.name.text = "000000"


        else:
            self.color_positive = "black"
            self.color_negative = "white"
            self.root.ids.name.text = "FFFFFF"



demo_class = layout_demo()
demo_class.run()