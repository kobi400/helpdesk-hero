from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.lang import Builder

Builder.load_file('Templates/HomeScreen.kv')


# created a class that inherits from MDScreenManager
class ScreenManager(MDScreenManager):
    pass


class HomeScreen(MDScreen):
    pass


class ChatUI(BoxLayout):
    pass
