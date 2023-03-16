# Quizz 41
## Python Part:
```python
import random
from kivymd.app import MDApp

class Layout(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.values = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.player = "X"
        self.opponent = "O"

    def build(self):
        return

    def button_press(self, button_id):
        button_id = str(button_id)
        current_player = self.player
        current_button = self.root.ids["button" + button_id]
        if self.values[int(button_id) - 1] == 0:
            current_button.text = current_player
            current_button.md_bg_color = "#B0D7FF" if current_player == "X" else "#EAE8FF"
            self.values[int(button_id) - 1] = 1 if current_player == "X" else 2

            # check for winning move
            for i in range(1, 10):
                if self.values[i - 1] == 0:
                    self.values[i - 1] = 2
                    if self.check_win(self.opponent):
                        self.root.ids.label2.text = "Winner is O"
                        self.disable_buttons()
                        return
                    self.values[i - 1] = 0

            # check for blocking move
            for i in range(1, 10):
                if self.values[i - 1] == 0:
                    self.values[i - 1] = 1
                    if self.check_win(self.player):
                        self.values[i - 1] = 2
                        current_button = self.root.ids["button" + str(i)]
                        current_button.text = self.opponent
                        current_button.md_bg_color = "#EAE8FF"
                        self.root.ids.label2.text = "Current Player: X"
                        return
                    self.values[i - 1] = 0

            # otherwise, choose a random move
            while True:
                i = random.randint(1, 9)
                if self.values[i - 1] == 0:
                    self.values[i - 1] = 2
                    current_button = self.root.ids["button" + str(i)]
                    current_button.text = self.opponent
                    current_button.md_bg_color = "#EAE8FF"
                    break

            # check for winner
            if self.check_win(self.opponent):
                self.root.ids.label2.text = "Winner is O"
                self.disable_buttons()
                return

            # check for tie
            if all(value != 0 for value in self.values):
                self.root.ids.label2.text = "It's a tie!"
                self.disable_buttons()
                return

            # switch player
            self.player, self.opponent = self.opponent, self

    def check_win(self, player):
        if player == "X":
            player_value = 1
        else:
            player_value = 2

        # check rows
        for i in range(1, 10, 3):
            if self.values[i - 1] == player_value and self.values[i] == player_value and self.values[i + 1] == player_value:
                return True

        # check columns
        for i in range(1, 4):
            if self.values[i - 1] == player_value and self.values[i + 2] == player_value and self.values[i + 5] == player_value:
                return True

        # check diagonals
        if self.values[0] == player_value and self.values[4] == player_value and self.values[8] == player_value:
            return True
        if self.values[2] == player_value and self.values[4] == player_value and self.values[6] == player_value:
            return True

        return False

    def disable_buttons(self):
        for i in range(1, 10):
            self.root.ids["button" + str(i)].disabled = True

    def reset(self):
        self.values = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(1, 10):
            self.root.ids["button" + str(i)].text = ""
            self.root.ids["button" + str(i)].disabled = False
            self.root.ids["button" + str(i)].md_bg_color = "#FFFFFF"
        self.root.ids.label2.text = "Current Player: X"
        self.player = "X"
        self.opponent = "O"

if __name__ == "__main__":
    Layout().run()
```
## KivyMD Part:
```kv
MDScreen:
    id : screen
    size:500,500
    MDBoxLayout:
        id: main_box
        size_hint: .8, .8
        orientation: 'vertical'
        pos_hint: {'center_x': .5, 'center_y': .5}
        MDBoxLayout:
            id: box1
            size_hint: 1, .2
            orientation: 'vertical'
            MDLabel:
                id: label1
                text: 'Tic Tac Toe by Bob'
                halign: 'center'
                font_style: 'H3'
            MDLabel:
                id: label2
                text: "Current Player:" + app.player
                halign: 'center'
                font_style: 'H5'

        MDBoxLayout:
            id: box2
            size_hint: 1, .8
            orientation: 'vertical'
            pos_hint: {'center_x': .5, 'center_y': .5}
            MDBoxLayout:
                id: layerone
                size_hint:1,.33
                orientation:"horizontal"
                MDRaisedButton:
                    id: button1
                    text: ""
                    size_hint: .33, 1
                    md_bg_color: "grey"
                    on_release: app.button_press("1")
                MDRaisedButton:
                    id: button2
                    text: ""
                    size_hint: .33, 1
                    md_bg_color: "grey"
                    on_release: app.button_press("2")
                MDRaisedButton:
                    id: button3
                    text: ""
                    size_hint: .33, 1
                    md_bg_color: "grey"
                    on_release: app.button_press("3")
            MDBoxLayout:
                id: layertwo
                size_hint:1,.33
                orientation:"horizontal"
                MDRaisedButton:
                    id: button4
                    text: ""
                    size_hint: .33, 1
                    md_bg_color: "grey"
                    on_release: app.button_press("4")
                MDRaisedButton:
                    id: button5
                    text: ""
                    size_hint: .33, 1
                    md_bg_color: "grey"
                    on_release: app.button_press("5")
                MDRaisedButton:
                    id: button6
                    text: ""
                    size_hint: .33, 1
                    md_bg_color: "grey"
                    on_release: app.button_press("6")

            MDBoxLayout:
                id: layerthree
                size_hint:1,.33
                orientation:"horizontal"
                MDRaisedButton:
                    id: button7
                    text: ""
                    size_hint: .33, 1
                    md_bg_color: "grey"
                    on_release: app.button_press("7")
                MDRaisedButton:
                    id: button8
                    text: ""
                    size_hint: .33, 1
                    md_bg_color: "grey"
                    on_release: app.button_press("8")
                MDRaisedButton:
                    id: button9
                    text: ""
                    size_hint: .33, 1
                    md_bg_color: "grey"
                    on_release: app.button_press("9")

        MDBoxLayout:
            id: resetbox
            size_hint: 1, .2
            orientation: 'vertical'
            MDRaisedButton:
                id: resetbutton
                text: "Reset"
                size_hint: .5, .75
                pos_hint: {'center_x': .5, 'center_y': .5}
                on_release: app.reset()
```

## Proof:
![](/Images/quizz41-proof.png)
