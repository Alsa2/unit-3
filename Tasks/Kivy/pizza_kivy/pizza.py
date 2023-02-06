from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.core.audio import SoundLoader


class IntroScreen(MDScreen):
    pass

class PrepareDoughtScreen(MDScreen):
    pass

class AddingTomatoScreen(MDScreen):
    pass

class AddingCheeseScreen(MDScreen):
    pass

class AddingToppingsScreen(MDScreen):
    pass

class FurnaceScreen(MDScreen):
    pass

class PizzaReadyScreen(MDScreen):
    pass

class recipe(MDApp):
    def on_start(self):
        sound = SoundLoader.load('assets/pizza_theme.mp3')
        sound.play()
        sound.loop = True

    def build(self):
        return

    


app = recipe()
app.run()