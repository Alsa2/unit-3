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
    