from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager
from kivy.core.audio import SoundLoader
from kivy.metrics import dp
from kivy.clock import Clock
from functools import partial
from random import randint

class Manager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()
        self.app.manager = self


class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()
        self.app.main = self

    pouscreen = ObjectProperty(None)
    curado_txt = ObjectProperty(None)


class TopMenu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()
        self.app.top_menu = self
        self.gameselect = GameSelect()
        self.light = Clock.schedule_interval(self.moneyattention, 1/7)

    money = ObjectProperty(None)
    level = ObjectProperty(None)
    moneybt = ObjectProperty(None)
    levelbt = ObjectProperty(None)
    g = 1
    multiply = 0.1

    def moneyattention(self, dt):
        self.g += self.multiply
        if self.g >= 1.8:
            self.multiply *= -1
        elif self.g <= 0.9:
            self.multiply *= -1
        self.moneybt.color = (self.g, self.g, self.g, 1)

    def on_touch_down(self, touch):
        if self.moneybt.collide_point(touch.x, touch.y):
            self.gameselect.open()
            self.moneybt.color = (1, 1, 1, 1)
            self.light.cancel()
        if self.levelbt.collide_point(touch.x, touch.y):
            Pix().open()


class Pix(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            webbrowser.open('https://livepix.gg/kenew')
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


class MenuBT(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.app.main.pouscreen.open()
            return
        self.dismiss()


class PauseScreen(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.dismiss()
            return
        self.dismiss()


class GameMenu(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.app.main.pouscreen.open()
            return
        self.dismiss()


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
