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


class GozaPeida(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()
        self.app.gozapeida = self


class CltRun(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()
        self.app.cltrun = self


class GameMenu(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.app.main.pouscreen.open()
            return
        self.dismiss()


class GameSelect(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()

    game1 = ObjectProperty(None)
    game2 = ObjectProperty(None)


class MusicSwitcher(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()

    state = 'on'

    def switch_music(self):
        if self.state == 'on':
            self.state = 'off'
            self.app.game_menu.background_music.stop()
            self.ids.music_switcher.text = 'Music: off'
        else:
            self.state = 'on'
            self.app.game_menu.background_music.play()
            self.ids.music_switcher.text = 'Music: on'


class MusicSwitcherButton(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.app.top_menu.switch_music()
            return
        self.dismiss()
