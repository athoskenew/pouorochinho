from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager
from kivy.core.audio import SoundLoader
from functools import partial
import threading
import webbrowser

from game_menu import GameMenu, GozaPeida, CltRun
from main_screen import MainScreen, Manager, TopMenu, Pix
from shop import Shop, ShopItem, Fridge, StackItem
from texts import Texts


class GozaPeidaApp(App):
    def build(self):
        manager = Manager()

        manager.add_widget(MainScreen(name='home'))
        manager.add_widget(GameMenu(name='game_menu'))
        manager.add_widget(GozaPeida(name='game1'))
        manager.add_widget(CltRun(name='game2'))

        return manager


if __name__ == '__main__':
    GozaPeidaApp().run()
