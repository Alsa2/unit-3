from kivymd.app import MDApp

class main(MDApp):
    def build(self):
        return
    def hello_world(self):
        print("Hello World")
        self.rood.ids.label.text = "Hello World"

demonstration = main()
demonstration.run()