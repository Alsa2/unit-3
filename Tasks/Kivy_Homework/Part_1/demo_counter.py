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