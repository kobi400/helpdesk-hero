from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from Components.customwidget import CustomWidget

Builder.load_file("main_app/app.kv")

class MainApp(MDApp):
    def build(self):
        return CustomWidget()

if __name__ == "__main__":
    MainApp().run()
