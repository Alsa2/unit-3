from kivymd.app import MDApp

class layout(MDApp):
    def build(self):
        return
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.grid = [[0,0,0],[0,0,0],[0,0,0]]
        self.turn = 1

    def button_pressed(self, button):
        if self.turn == 1:
            self.root.ids.button[button].text = "X"
            self.turn = 2
            self.root.ids.main_screen.turn_label.text = "O's Turn"
        else:
            self.root.ids.button[button].text = "O"
            self.turn = 1
            self.root.ids.main_screen.turn_label.text = "X's Turn"

        self.root.ids.button[button].disabled = True
        

tiktaktoe = layout()
tiktaktoe.run()