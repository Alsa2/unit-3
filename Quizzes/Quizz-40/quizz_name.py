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