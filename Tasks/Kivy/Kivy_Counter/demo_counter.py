from kivymd.app import MDApp

class layout_demo(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.count = 0

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
        self.title = "Kivy Counter"
        return

    def change(self, name:str):
        if "up" in name:
            self.count += 1
        elif "down" in name:
            self.count -= 1
        
        self.root.ids.counter_label.text = f"x= {self.count}"

    def set_counter(self, value):
        user_start = int(self.root.ids.user_start_x.text)
        self.count = user_start
        self.root.ids.counter_label.text = f"x= {self.count}"
        

demo_class = layout_demo()
demo_class.run()
    
        