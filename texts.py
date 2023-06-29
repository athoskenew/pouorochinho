from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager
from kivy.core.audio import SoundLoader
from kivy.uix.label import Label
from functools import partial
from random import randint


class Manager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()
        self.app.manager = self


class Texts(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()

    texts = ObjectProperty(None)


class TextItem(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.open()
            return
        self.dismiss()

    def open(self):
        if self.app.main.pouscreen.textsbutton.available:
            self.app.main.pouscreen.textsbutton.available = False
            self.app.main.pouscreen.textsbutton.color = [0, 0, 0, 1]
            self.app.main.pouscreen.textsbutton.text = 'Locked'

            if self.app.main.curado_txt.text == '':
                self.app.main.curado_txt.text += 'CURADO'
            else:
                self.app.main.curado_txt.text += ', CURADO'
