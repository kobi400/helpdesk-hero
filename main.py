from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from screens.loginscreen import LoginScreen
from screens.homescreen import HomeScreen
from screens.reset import ResetPasswordScreen
from screens.signupscreen import SignupScreen
from kivy.lang import Builder

Builder.load_file('Templates/LoginScreen.kv')
Builder.load_file('Templates/SignupScreen.kv')
Builder.load_file('Templates/ResetPasswordScreen.kv')


class MyApp(MDApp):
    def build(self):
        kv = Builder.load_file('main.kv')

        # Initialize the ScreenManager
        screen_manager = ScreenManager()

        # Create instances of your screens
        login_screen = LoginScreen(name='login')
        signup_screen = SignupScreen(name='signup')
        reset_password_screen = ResetPasswordScreen(name='reset')

        # Add screens to the ScreenManager
        screen_manager.add_widget(login_screen)
        screen_manager.add_widget(signup_screen)
        screen_manager.add_widget(reset_password_screen)

        # Set the initial screen (optional)
        screen_manager.current = 'login'

        return kv


if __name__ == "__main__":
    MyApp().run()
