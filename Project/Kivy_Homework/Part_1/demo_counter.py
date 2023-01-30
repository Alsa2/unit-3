from kivymd.app import MDApp

class layout_demo(MDApp):
    def build(self):
        return
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.original = 0
        self.output = 0

    def currency_converter(self, currency:str):
        pass



demo_class = layout_demo()
demo_class.run()