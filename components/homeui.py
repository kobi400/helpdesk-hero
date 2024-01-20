from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField


class ChatUI(BoxLayout):
    chat_display = MDLabel()
    text_input = MDTextField(multiline=False)
    send_button = MDIconButton(text="Send")

    def __init__(self, **kwargs):
        super(ChatUI, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_widget(self.chat_display)
        self.add_widget(self.text_input)
        self.add_widget(self.send_button)

    def send_message(self, button):
        message = self.text_input.text
        self.chat_display.text += f"\n[You]: {message}"
        self.text_input.text = ""


class TextLayout(MDTextField):
    def __init__(self, **kwargs):
        super(TextLayout, self).__init__(**kwargs)
        self.text_field = MDTextField()

    def clear_text(self):
        self.text_field.text = ''
