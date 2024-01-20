from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class CustomWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(CustomWidget, self).__init__(**kwargs)
        self.add_widget(Button(text="Custom Button"))
