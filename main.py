# -*- coding: utf-8 -*-
import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"
os.environ['PYTHONWARNINGS'] = 'ignore:.*'
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.properties import BooleanProperty
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
import threading
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.clock import Clock
from functools import partial
from random import randint
from kivy.uix.screenmanager import ScreenManager
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.core.window import Window
import sys
from kivy.resources import resource_add_path, resource_find
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch')

kv = """
# -*- coding: utf-8 -*-
#:import Hexad kivy.utils.get_color_from_hex

<ImageButton>:

<ItemImage>:
    size_hint: None, None
    size: dp(50), dp(50)

<GameMenu>:
    home: home
    moneygained: moneygained
    canvas.before:
        Color:
            rgba: 1, 0.7608, 0.7725, 1
        Rectangle:
            pos: self.pos
            size: self.size
    size_hint_y: None
    height: dp(50)
    padding: dp(5)
    FloatLayout:
        size_hint_x: None
        width: dp(50)
        ContextButton:
            id: home
            width: dp(40)
            source: 'source/images/home.png'
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    Widget:
    Widget:
    Widget:
    FloatLayout:
        id: moneygainedfl
        size_hint_x: None
        width: dp(50)
        ContextButton:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint_x: None
            width: dp(50)
            source: 'source/images/moeda.png'
        Texts:
            id: moneygained
            pos_hint: {'center_x': 0.43, 'center_y': 0.5}
            color: 1, 1, 1, 1
            outline_color: 0, 0, 0, 1
            text: '0'

<Projetil>:
    size_hint: None, None
    size: dp(20), dp(40)
    source: 'source/images/projetil.png'

<GozaPeida>:
    orientation: 'vertical'
    pougame: pougame
    poufemea: poufemea
    gamefl: gamefl
    menu: menu
    canvas:
        Color:
            rgba: Hexad("#C1CFDA")
        Rectangle:
            size: self.size
            pos: self.pos
            source: 'source/images/floresta.png'
    GameMenu:
        id: menu
    FloatLayout:
        id: gamefl
        Image:
            id: poufemea
            size_hint: None, None
            size: dp(50), dp(50)
            x: root.x + root.width/2 - dp(25)
            y: root.y + root.height - dp(150)
            source: 'source/images/poufemea.png'
        Image:
            id: pougame
            size_hint: None, None
            size: dp(50), dp(50)
            x: root.x + root.width/2 - dp(25)
            y: root.y + 10
            source: 'source/images/poufeliz.png'

<Clt>:
    color: 1,1,1,1
    canvas:
        Color:
            rgba: self.color
        Rectangle:
            size: self.size
            pos: self.pos
            source: 'source/images/clt.png'
    size_hint: None, None
    size: dp(30), dp(40)

<CltRun>:
    orientation: 'vertical'
    menu: menu
    gamefl: gamefl
    pougame: pougame

    canvas:
        Color:
            rgba: Hexad("#C1CFDA")
        Rectangle:
            size: self.size
            pos: self.pos
            source: 'source/images/city.jpg'
    GameMenu:
        id: menu
    FloatLayout:
        id: gamefl
        Image:
            id: pougame
            size_hint: None, None
            size: dp(50), dp(50)
            x: root.x + root.width/2 - dp(25)
            y: root.y + 10
            source: 'source/images/poufeliz.png'

<GameSelect>:
    size_hint: 0.5, 0.3
    title: 'Selecione um jogo'
    title_align: 'center'
    title_color: 'black'
    title_font: 'source/font/ComicSans'
    title_size: dp(20)
    separator_height: 0
    background_color: 1, 1, 1, 0.8
    background: ''
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        Button:
            font_size: 18
            size_hint: None, None
            size: 200, 50
            pos_hint: {'center_x': 0.5}
            background_normal: ''
            background_color: 0.8, 0.2, 0.2, 1
            # background_down: ''
            text: 'Goza e peida'
            on_release: root.game1()
        Button:
            font_size: 18
            size_hint: None, None
            size: 200, 50
            pos_hint: {'center_x': 0.5}
            background_normal: ''
            background_color: 0.8, 0.2, 0.2, 1
            # background_down: ''
            text: 'CLT Run'
            on_release: root.game2()

<Pix>:
    size_hint: 0.7, 0.7
    title: 'ME MANDE SEU DINHEIRO'
    title_align: 'center'
    title_color: 'black'
    title_font: 'source/font/ComicSans'
    title_size: dp(20)
    separator_height: 0
    background_color: 1, 1, 1, 0.8
    background: ''
    Image:
        source: 'source/images/livepix.png'

<Pou>:
    size_hint: None, None
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size: dp(100), dp(100)
    boca: boca
    cabelo: 'cabelo.png'
    hair_style: hair
    pou: pou
    source: 'source/images/pourochi.png'
    offsetcx: 0
    offsetcy: 0
    offsetcw: 0
    offsetch: 0
    eye_offset_x: 0
    eye_offset_y: 0
    Widget:
        id: pou
        canvas:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                source: root.source
                size: root.size[0], root.size[1] - 4
                pos: root.pos
    Widget:
        canvas:
            Color:
                rgba: 1,1,1,1
            Rectangle:
                source: 'source/images/' + root.cabelo
                pos: root.x + dp(9) + root.offsetcx, root.y + dp(55) + root.offsetcy
                size: dp(85) + root.offsetcw, dp(43) + root.offsetch
        id: hair
        size_hint: None, None
        #width: dp(85) + root.offsetcw
        #height: dp(100) + root.offsetch
        #pos: root.x + dp(9) + root.offsetcx, root.y + dp(28) + root.offsetcy


    Widget:
        canvas:
            Color:
                rgba: 0, 0, 0, 1
            Ellipse:
                size: dp(8), dp(8)
                pos: root.x + dp(36) + dp(root.eye_offset_x), root.y + dp(63) + dp(root.eye_offset_y)
    Widget:
        canvas:
            Color:
                rgba: 0, 0, 0, 1
            Ellipse:
                size: dp(8), dp(8)
                pos: root.x + dp(52) + dp(root.eye_offset_x), root.y + dp(63) + dp(root.eye_offset_y)
    Widget:
        id: boca
        top_offset: 20
        down_offset: 20
        canvas:
            Color:
                rgba: 1,0,0,1
            Color:
                rgba: 0, 0, 0, 1
            Line:
                width: 2
                bezier: [root.x + dp(33), root.y + dp(30), root.x + dp(47), root.y + dp(self.top_offset), root.x + dp(62), root.y + dp(30)]
            Line:
                bezier: [root.x + dp(33), root.y + dp(30), root.x + dp(47), root.y + dp(self.down_offset), root.x + dp(62), root.y + dp(30)]
                width: 2
<Texts>:
    size_hint_y: 0.3
    text: 'Comidinha'
    color: 0, 0, 0, 1
    outline_color: 1, 1, 1, 1
    outline_width: 2
    font_name: 'source/font/ComicSans'
    bold: True

<StackItem>:
    orientation: 'vertical'
    size_hint: None, None
    height: dp(150)
    source: ''
    item: ''
    Image:
        source: root.source
    Texts:
        text: root.item
        size: self.texture_size
        text_size: root.width - dp(5), None
        halign: 'center'

<ShopItem>:
    size_hint: 1, None
    height: dp(100)
    img: ''
    name: ''
    description: ''
    price: ''
    buy: buy
    BoxLayout:
        Image:
            source: root.img
        BoxLayout:
            id: iteminfo
            padding: dp(5)
            orientation: 'vertical'
            Texts:
                text: root.name
                color: 1, 1, 1, 1
                outline_color: 0, 0, 0, 1
                outline_width: 2
                text_size: iteminfo.width - dp(5), None
                size: self.texture_size
            Texts:
                text: root.description
                font_size: dp(12)
                text_size: iteminfo.width - dp(5), None
                outline_width: 0
                size: self.texture_size
        BoxLayout:
            orientation: 'vertical'
            BoxLayout:
                Image:
                    size_hint: 0.3, 1
                    source: 'source/images/moeda.png'
                Texts:
                    size_hint_y: 1
                    text: root.price
            Image:
                id: buy
                source: 'source/images/buy.png'

<Fridge>:
    itens: itens
    size_hint: 0.9, 0.95
    title: 'Geladeira'
    title_align: 'center'
    title_color: 'black'
    title_font: 'source/font/ComicSans'
    title_size: dp(20)
    separator_height: 0
    background_color: 1, 1, 1, 0.8
    background: ''
    StackLayout:
        id: itens
        spacing: dp(15), 0

<Shop>:
    size_hint: 0.8, 0.9
    title: 'Shop'
    title_align: 'center'
    title_color: 'black'
    title_font: 'source/font/ComicSans'
    title_size: dp(20)
    separator_height: 0
    background_color: 1, 1, 1, 0.8
    background: ''
    box: b1
    ScrollView:
        always_overscroll: False
        effect_cls: 'ScrollEffect'
        BoxLayout:
            id: b1
            height: self.minimum_height
            size_hint_y: None
            orientation: 'vertical'
            spacing: dp(15)


<PouScreen>:
    canvas.before:
        Color:
            rgba: 1, 0.49, 0.48, 1
        Rectangle:
            pos: self.pos
            size: self.size


<ContextButton@Widget>:
    source: ''
    size_hint_x: None
    width: dp(50)
    color: 1, 1, 1, 1
    canvas:
        Color:
            rgba: self.color
        Rectangle:
            pos: self.pos
            size: self.size
            source: self.source

<TopMenu>:
    money: money
    level: level
    moneybt: moneybt
    levelbt: levelbt
    canvas.before:
        Color:
            rgba: 1, 0.7608, 0.7725, 1
        Rectangle:
            pos: self.pos
            size: self.size
    size_hint_y: None
    height: dp(50)
    padding: dp(5)
    FloatLayout:
        id: flmoeda
        size_hint_x: None
        width: dp(50)
        ContextButton:
            id: moneybt
            source: 'source/images/moeda.png'
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        Texts:
            id: money
            pos: flmoeda.x + dp(13), flmoeda.y
            color: 1, 1, 1, 1
            outline_color: 0, 0, 0, 1
            text: '100'
    Widget:
    BoxLayout:
        size_hint_x: None
        width: dp(200)
        spacing: dp(5)
        ContextButton:
            source: 'source/images/coxinha.png'
        ContextButton:
            source: 'source/images/cura.png'
        ContextButton:
            source: 'source/images/poudoido.png'
        ContextButton:
            source: 'source/images/raio.png'
    Widget:
    FloatLayout:
        id: fllevel
        size_hint_x: None
        width: dp(50)
        ContextButton:
            id: levelbt
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint_x: None
            width: dp(50)
            source: 'source/images/level.png'
        Texts:
            id: level
            pos: fllevel.x, fllevel.y + dp(10)
            color: 1, 1, 1, 1
            outline_color: 0, 0, 0, 1
            text: '1'


<BottomMenu>:
    canvas.before:
        Color:
            rgba: 0.5804, 0.2824, 0.2588, 1
        Rectangle:
            pos: self.pos
            size: self.size
    size_hint_y: None
    height: dp(50)
    padding: dp(5)
    i_img: item_img
    i_text: item_text
    left_arrow: left
    right_arrow: right
    fridge: fridge_button
    shop: shop_button
    FloatLayout:
        id: fridge
        size_hint_x: None
        width: dp(70)
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(100)
            pos: fridge.pos
            ContextButton:
                id: fridge_button
                size_hint: None, 0.8
                width: fridge.width
                source: 'source/images/fridge.png'
            Texts:
                size_hint_y: 0.2
                text: 'Geladeira'
    Widget:
    FloatLayout:
        id: item
        size_hint_x: None
        width: dp(200)
        BoxLayout:
            orientation: 'vertical'
            size_hint_x: None
            size_hint_y: None
            height: dp(80)
            width: dp(200)
            x: item.x
            y: item.y
            BoxLayout:
                size_hint_y: 0.7
                Widget:
                    id: left
                    canvas:
                        Color:
                            rgba: 1, 1, 1, 1
                        Rectangle:
                            pos: self.pos
                            size: self.size
                            source: 'source/images/left.png'
                Widget:
                    id: item_img
                    source: 'cherry.png'
                    woffset: 0
                    canvas:
                        Rectangle:
                            size: item_img.width + item_img.woffset, item_img.height
                            pos: self.pos[0] + (-1)*self.woffset/2, self.pos[1]
                            source: 'source/images/' + self.source
                Widget:
                    id: right
                    canvas:
                        Color:
                            rgba: 1, 1, 1, 1
                        Rectangle:
                            pos: self.pos
                            size: self.size
                            source: 'source/images/right.png'
            Texts:
                id: item_text
                text: 'Cherries'
    Widget:
    FloatLayout:
        id: shop
        size_hint_x: None
        width: dp(70)
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(100)
            pos: shop.pos
            ContextButton:
                id: shop_button
                size_hint: None, 0.8
                width: shop.width
                source: 'source/images/shop.png'
            Texts:
                size_hint_y: 0.2
                text: 'Shop'


<MainScreen>:
    pouscreen: pou_screen
    curado_txt: curado_txt
    orientation: 'vertical'
    TopMenu:
        id: top
    PouScreen:
        id: pou_screen
        Texts:
            id: curado_txt
            opacity: 0
            text: 'Curado da Calvice!'
            pos_hint: {'top': 0.8, 'center_x': 0.5}
        Pou:
    BottomMenu:
        id: bottom
        pou_screen: pou_screen


<Manager>:
    Screen:
        name: 'home'
        MainScreen:
    Screen:
        name: 'game1'
        GozaPeida:

    Screen:
        name: 'game2'
        CltRun:
"""

Builder.load_string(kv)

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


class GameMenu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()

    home = ObjectProperty(None)

    def on_touch_down(self, touch):
        if self.home.collide_point(touch.x, touch.y):
            if self.app.manager.current == 'game1':
                self.app.game1.moving()

            if self.app.manager.current == 'game2':
                self.app.game2.moving()

            self.app.manager.current = 'home'
            self.moneygained.text = '0'


class Projetil(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()
        self.game = self.app.game1
        self.topmenu = self.app.top_menu

    disparo = None
    colisao = None
    colided = False
    femeashot = False

    def movimentar(self, dt):
        if self.femeashot:
            if self.y + self.height > 0:
                self.y -= 30
            else:
                self.gatilho()
                self.game.gamefl.remove_widget(self) # saiu da tela
        else:
            if self.y < self.game.gamefl.height - self.height:
                self.y += 10
            else:
                self.gatilho()
                self.game.gamefl.remove_widget(self)
                if self.game.tiros > 0:
                    self.game.tiros -= 1

    def colisionverify(self, dt):
        if not self.colided and not self.femeashot:
            if self.collide_widget(self.game.poufemea):
                self.colided = True
                self.topmenu.money.text = str(int(self.topmenu.money.text) + 50)
                self.game.menu.moneygained.text = str(int(self.game.menu.moneygained.text) + 50)
                self.gatilho()
                if self.game.peido_sound is not None:
                    self.game.peido_sound.play()
                if self.game.tiros > 0:
                    self.game.tiros -= 1
                self.game.gamefl.remove_widget(self)

    def gatilho(self):
        if self.femeashot:
            if self.disparo is None:
                self.disparo = Clock.schedule_interval(self.movimentar, 1 / 24)
            else:
                self.disparo.cancel()
        else:
            if self.disparo is None:
                self.disparo = Clock.schedule_interval(self.movimentar, 1/24)
                self.colisao = Clock.schedule_interval(self.colisionverify, 1 / 30)

            else:
                self.disparo.cancel()
                self.colisao.cancel()

    # on_y utilizado no lugar de colisionverify para verificar a colisão com o pou
    # essa abordagem é mais correta que usar um clock, mas vou deixar a outra
    # visível aí

    def on_y(self, prop, value):
        if self.femeashot:
            if self.collide_widget(self.game.pougame): #and int(self.topmenu.money.text) > 0:
                self.colided = True
                self.topmenu.money.text = str(int(self.topmenu.money.text) - 5)
                self.game.menu.moneygained.text = str(int(self.game.menu.moneygained.text) - 5)
                self.gatilho()
                self.game.gamefl.remove_widget(self)


class GozaPeida(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()
        self.app.game1 = self
        self.move = None  # Clock.schedule_interval(self.move_femea, 1/30)
        self.lock = False
        self.peido_sound = None

    menu = ObjectProperty(None)
    gamefl = ObjectProperty(None)
    pougame = ObjectProperty(None)
    poufemea = ObjectProperty(None)
    movimento = randint(3, 7)
    tiros = 0

    def moving(self):
        if self.lock:
            self.move.cancel()
            self.peido_sound = None
            self.lock = False
        else:
            self.peido_sound = SoundLoader.load('source/audios/sfx/peido.mp3')
            self.move = Clock.schedule_interval(self.move_femea, 1/30)
            self.lock = True

    def move_femea(self, dt):
        self.poufemea.x += self.movimento
        if randint(1, 20) == 5:
            disp = Projetil(x=self.poufemea.x, y=self.poufemea.y)
            disp.color = (1, 0, 0, 1)
            disp.femeashot = True
            self.gamefl.add_widget(disp)
            disp.gatilho()
        if self.poufemea.x + self.poufemea.width > self.width:
            self.movimento = -randint(3, 10)
        elif self.poufemea.x < self.x:
            self.movimento = +randint(3, 10)

    def on_touch_down(self, touch):
        if self.gamefl.collide_point(touch.x, touch.y):
            if self.tiros <= 2:
                disp = Projetil(x=touch.x, y=self.pougame.y)
                self.gamefl.add_widget(disp)
                disp.gatilho()
                self.tiros += 1
            self.pougame.x = touch.x
        return super(GozaPeida, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        if self.gamefl.collide_point(touch.x, touch.y):
            self.pougame.x = touch.x
        return super(GozaPeida, self).on_touch_move(touch)


class Clt(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()
        self.game = self.app.game2
        self.pougame = self.game.pougame
        self.topmenu = self.app.top_menu
        self.clk_move = Clock.schedule_interval(self.move, 1 / 30)
        self.velocidade = randint(5, 20)
    colidiu = False
    passou = False

    def move(self, dt):
        self.x -= self.velocidade

    def on_x(self, prop, value):
        if self.x < self.game.gamefl.x:
            self.game.gamefl.remove_widget(self)
            self.clk_move.cancel()
        if self.collide_widget(self.pougame) and not self.colidiu:
            self.topmenu.money.text = str(int(self.topmenu.money.text) - 5)
            self.game.menu.moneygained.text = str(int(self.game.menu.moneygained.text) - 5)
            self.colidiu = True
            self.color = (1, 0, 0.7, 1)
        if self.x < self.pougame.x and not self.colidiu and not self.passou:
            self.passou = True
            self.topmenu.money.text = str(int(self.topmenu.money.text) + 50)
            self.game.menu.moneygained.text = str(int(self.game.menu.moneygained.text) + 50)


class CltRun(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()
        self.app.game2 = self

    menu = ObjectProperty(None)
    gamefl = ObjectProperty(None)
    pougame = ObjectProperty(None)
    pulo = 24
    # jumping = False
    clk_pulo = None
    clk_clt = None

    def moving(self):
        if self.clk_pulo is None:
            self.clk_pulo = Clock.schedule_interval(self.fall, 1 / 30)
            self.clk_clt = Clock.schedule_interval(self.gerarclt, 1.5)
        else:
            self.clk_pulo.cancel()
            self.clk_clt.cancel()
            self.clk_clt = None
            self.clk_pulo = None

    def gerarclt(self, dt):
        clt = Clt()
        clt.y = self.pougame.y
        clt.x = self.gamefl.width + clt.width
        self.gamefl.add_widget(clt)

    def jump(self):
        if self.pougame.y < self.gamefl.y + 100:
            self.pougame.y += self.pulo

    def fall(self, dt):
        if self.pougame.y > self.gamefl.y + 11:
            self.pougame.y -= 2

    def on_touch_down(self, touch):
        if self.gamefl.collide_point(touch.x, touch.y):
            self.jump()
        return super(CltRun, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        return super(CltRun, self).on_touch_up(touch)


class Texts(Label):
    pass


class GameSelect(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()

    game1_play = False

    def game1(self):
        self.dismiss()
        self.app.game1.moving()
        self.app.manager.current = 'game1'

    def game2(self):
        self.dismiss()
        self.app.game2.moving()
        self.app.manager.current = 'game2'


class Pix(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()


class TopMenu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()
        self.app.top_menu = self
        self.gameselect = GameSelect()
        self.light = Clock.schedule_interval(self.moneyattention, 1/7)

    money = ObjectProperty(None)
    level = ObjectProperty(None)
    # Fazendo o dinheiro e level serem botões
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


class StackItem(BoxLayout):
    def __init__(self, source, item, **kwargs):
        super().__init__(**kwargs)
        self.source = source
        self.item = item
        self.app = App.get_running_app()

    def inlist(self, l1, item):
        add = False
        for i in l1:
            if i['name'] == item:
                add = True
        if add is not True:
            l1.append({'name': item, 'image': self.source.split('/')[2]})

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.app.fridge.dismiss()
            addlist = threading.Thread(target=self.inlist, args=(self.app.bottom_menu.food, self.item))
            addlist.start()
            self.app.fridge.itens.remove_widget(self)


class Fridge(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()
        self.app.fridge = self

    itens = ObjectProperty(None)
    in_fridge = []


class ShopItem(BoxLayout):
    def __init__(self, name, price, img, description, **kwargs):
        super().__init__(**kwargs)
        self.img = img
        self.name = name
        self.description = description
        self.price = price
        self.app = App.get_running_app()
        self.dinheiro_sound = None

    buy = ObjectProperty(None)

    def removeinfo(self, widget, dt):
        self.buy.remove_widget(widget)

    def on_touch_up(self, touch):
        if self.buy.collide_point(touch.x, touch.y):
            dinheiro = self.app.top_menu.money
            if int(self.price) > int(dinheiro.text):
                info = Texts(text="Sem dinheiro")
                info.center = self.buy.center
                self.buy.add_widget(info)
                Clock.schedule_once(partial(self.removeinfo, info), 1)

            else:
                geladeira = self.app.fridge
                if self.name in geladeira.in_fridge:
                    info = Texts(text="Ja possui!")
                    info.size = self.buy.texture_size
                    info.center = self.buy.center
                    self.buy.add_widget(info)
                    Clock.schedule_once(partial(self.removeinfo, info), 1)
                    return True
                self.dinheiro_sound = SoundLoader.load('source/audios/sfx/dinheiro.mp3')
                if self.dinheiro_sound is not None:
                    self.dinheiro_sound.play()
                geladeira.in_fridge.append(self.name)
                geladeira.itens.add_widget(StackItem(source=self.img, item=self.name))
                dinheiro.text = str(int(dinheiro.text) - int(self.price))
                self.app.shop.dismiss()
                if not self.app.shop.first_shop:
                    self.app.shop.first_shop = True


class Shop(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.standard_itens()
        self.app = App.get_running_app()
        self.app.shop = self
        self.first_info = Texts(text='Sua compra esta na geladeira!', pos_hint={'top': 0.8, 'center_x': 0.5})

    box = ObjectProperty(None)
    first_shop = BooleanProperty(False)

    def on_first_shop(self, prop, value):
        self.app.main.pouscreen.add_widget(self.first_info)
        Clock.schedule_once(self.remove_info, 10)

    def remove_info(self, dt):
        self.app.main.pouscreen.remove_widget(self.first_info)

    def standard_itens(self):
        self.box.add_widget(ShopItem(name='Potion da Calvicie', price='100', img='source/images/pocao1.png',
                                     description='Elimina sua calvicie instantaneamente.'))
        self.box.add_widget(ShopItem(name='Potion da Pica', price='200', img='source/images/pocao2.png',
                                     description='Te deixa pica.'))
        self.box.add_widget(ShopItem(name='Potion da Mitada', price='500', img='source/images/pocao3.png',
                                     description='Voce fala mitadas e ironias.'))
        self.box.add_widget(ShopItem(name='Potion da Supresa', price='500', img='source/images/pocao5.png',
                                     description='O que acontece? Surpresa.'))
        self.box.add_widget(ShopItem(name='Potion da Preguica', price='1000', img='source/images/pocao4.png',
                                     description='Fiquei com preguica de fazer essa.'))


class ItemImage(Image):
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()
        self.name = name

    def consumir(self):
        if self.app.pou.collide_point(self.x, self.y):
            if self.name == 'Potion da Calvicie':
                self.app.bottom_menu.index -= 1
                self.app.bottom_menu.left_arrowfn()
                self.app.fridge.in_fridge.remove(self.name)
                self.app.bottom_menu.food.remove({'image': 'pocao1.png', 'name': self.name})
                self.app.pou.calvo = False
            elif self.name == 'Potion da Pica':
                if self.app.pou.pica:
                    self.app.pou.pica = False
                else:
                    self.app.pou.pica = True
                    sound = SoundLoader.load('source/audios/sfx/potion.mp3')
                    if sound:
                        sound.play()
            elif self.name == 'Potion da Mitada':
                sound = SoundLoader.load('source/audios/mitadas/mitada{}.mp3'.format(randint(1, 35)))
                if sound:
                    sound.play()
            elif self.name == 'Potion da Supresa':
                sound = SoundLoader.load('source/audios/sfx/dinheiro.mp3')
                if sound:
                    sound.play()
                self.app.top_menu.money.text = str(int(self.app.top_menu.money.text) + randint(-100, 200))

            else:
                sound = SoundLoader.load('source/audios/sfx/comendo.mp3')
                if sound:
                    sound.play()


def imageoffset(name):
    if name == 'banana':
        return -40
    elif name == 'pica':
        return -25
    else:
        return 0


class BottomMenu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.popfridge = Fridge()
        self.popshop = Shop()
        self.app = App.get_running_app()
        self.app.bottom_menu = self
        self.hmm_sound = None

    i_img = ObjectProperty(None)
    i_text = ObjectProperty(None)
    left_arrow = ObjectProperty(None)
    right_arrow = ObjectProperty(None)
    fridge = ObjectProperty(None)
    shop = ObjectProperty(None)
    pou_screen = ObjectProperty(None)
    moving = {'active': False, 'object': None}
    hmm = False

    food = [{'image': 'cherry.png', 'name': 'cherry'},
            {'image': 'banana.png', 'name': 'banana'},
            {'image': 'pica.png', 'name': 'pica'}
            ]
    index = 0

    def open_fridge(self):
        self.popfridge.open()

    def open_shop(self):
        self.popshop.open()

    def left_arrowfn(self):
        actualfood = self.food[self.index]
        self.i_img.source = actualfood['image']
        self.i_text.text = actualfood['name']
        self.i_img.woffset = imageoffset(actualfood['name'])

    def on_touch_down(self, touch):
        if self.i_img.collide_point(touch.x, touch.y):
            img = ItemImage(source='source/images/' + self.i_img.source, name=self.i_text.text)
            self.pou_screen.add_widget(img)
            self.moving['active'] = True
            self.moving['object'] = img
            if self.hmm_sound is None:
                self.hmm_sound = SoundLoader.load('source/audios/sfx/hmm.mp3')

        if self.left_arrow.collide_point(touch.x, touch.y):
            if self.index != 0:
                self.index -= 1
                self.left_arrowfn()

        if self.right_arrow.collide_point(touch.x, touch.y):
            if self.index != len(self.food) - 1:
                self.index += 1
                actualfood = self.food[self.index]
                self.i_img.source = actualfood['image']
                self.i_img.woffset = imageoffset(actualfood['name'])
                self.i_text.text = actualfood['name']

        if self.fridge.collide_point(touch.x, touch.y):
            self.open_fridge()
        if self.shop.collide_point(touch.x, touch.y):
            self.open_shop()

        return super(BottomMenu, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        if self.moving['active']:
            self.moving['object'].center = touch.x, touch.y
            # movimento da boca
            if abs(self.moving['object'].center_y - self.app.pou.center_y) < dp(150) and \
                    abs(self.moving['object'].center_x - self.app.pou.center_x) < dp(150):
                if self.app.pou.boca.top_offset <= 70:
                    self.app.pou.boca.top_offset += 2
                    self.app.pou.boca.down_offset -= 0.4
                    if not self.hmm:
                        self.hmm = True
                        if self.hmm_sound is not None:
                            self.hmm_sound.play()
            else:
                if self.app.pou.boca.top_offset >= 20:
                    self.app.pou.boca.top_offset -= 2
                    self.app.pou.boca.down_offset += 0.4
            # movimento dos olhos
            if self.moving['object'].center_y - self.app.pou.center_y < dp(50):
                if self.app.pou.eye_offset_y > -2:
                    self.app.pou.eye_offset_y -= 0.1
            elif self.moving['object'].center_y - self.app.pou.center_y > dp(50):
                if self.app.pou.eye_offset_y < 2:
                    self.app.pou.eye_offset_y += 0.1

            if self.moving['object'].center_x - self.app.pou.center_x < dp(-10):
                if self.app.pou.eye_offset_x > -2:
                    self.app.pou.eye_offset_x -= 0.1
            elif self.moving['object'].center_x - self.app.pou.center_x > dp(10):
                if self.app.pou.eye_offset_x < 2:
                    self.app.pou.eye_offset_x += 0.1
            else:
                self.app.pou.eye_offset_x = 0

    def on_touch_up(self, touch):
        if self.moving['active']:
            if self.hmm:
                self.hmm = False
            self.app.pou.boca.top_offset = 20
            self.app.pou.boca.down_offset = 20
            self.app.pou.eye_offset_y = 0
            self.app.pou.eye_offset_x = 0
            self.moving['active'] = False
            consumir = threading.Thread(target=self.moving['object'].consumir)
            consumir.start()
            self.pou_screen.remove_widget(self.moving['object'])
            del self.moving['object']
            self.moving['object'] = None


class PouScreen(FloatLayout):
    pass


class Pou(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()
        self.app.pou = self
        self.cc = Clock.schedule_interval(self.calvar, randint(randint(3, 10), randint(15, 20)))
        self.calvices = self.app.calvices

    boca = ObjectProperty(None)
    calvo = BooleanProperty(False)
    hair_style = ObjectProperty(None)
    calvou = 0
    pica = BooleanProperty(False)
    pou = ObjectProperty(None)

    def showcurado(self, dt):
        """"Gambiarra pq o kivy não deixava fazer isso em outra thread"""
        self.app.main.curado_txt.opacity = 1

    def curado(self, dt):
        self.app.main.pouscreen.remove_widget(self.app.main.curado_txt)

    def calvar(self, dt):
        self.calvo = True

    def on_pica(self, prop, value):
        if value:
            self.source = 'source/images/poupica.png'
            if self.calvo:
                self.offsetcw = -dp(65)
                self.offsetcx = dp(29)
                self.offsetcy = dp(22)
        else:
            self.source = 'source/images/pourochi.png'
            if self.calvo:
                self.offsetcw = -dp(48)
                self.offsetcx = dp(22)
                self.offsetcy = dp(20)

    def on_calvo(self, prop, value):
        if value:
            self.offsetcw = -dp(48)
            self.offsetch = -dp(25)
            self.offsetcx = dp(22)
            self.offsetcy = dp(20)
            if self.pica:
                self.offsetcw = -dp(65)
                self.offsetcx = dp(29)
                self.offsetcy = dp(22)
            self.cabelo = 'calvice.png'
        else:
            self.offsetcw = 0
            self.offsetch = 0
            self.offsetcx = 0
            self.offsetcy = 0
            self.cabelo = 'cabelo.png'
            self.calvou += 1
            sound = SoundLoader.load('source/audios/sfx/potion.mp3')
            if sound:
                sound.play()
            if self.calvou >= self.calvices:
                Clock.schedule_once(self.showcurado)  # talvez não precise disso...
                Clock.schedule_once(self.curado, 10)
                self.cc.cancel()


class ImageButton:
    pass


class Pourochi(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    """
    Variáveis globais

    Normalmente isso não é recomendado, seria mais seguro linkar esses valores
    dentro de uma classe usando ids, mas, assim é mais fácil de gerenciar essas variáveis
    que serão usadas por diversas classes.

    Não repita isso (não sempre).

    """
    calvices = randint(2, 3)
    main = None
    top_menu = None
    bottom_menu = None
    fridge = None
    shop = None
    pou = None
    manager = None
    game1 = None
    game2 = None

    def build(self):
        self.icon = 'icon.ico'
        pou = Manager()
        return pou


if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    Pourochi().run()
