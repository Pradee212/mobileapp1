from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.label import Label
from myfirebase import MyFirebase
from kivy.core.window import Window

class HomeScreen(Screen) :
    pass
class FirstScreen(Screen) :
    pass
class SettingsScreen(Screen) :
    pass

class LoginScreen(Screen) :
    pass

class SignUpScreen(Screen) :
    pass

class ForgotPasswordScreen(Screen) :
    pass

class LabelButton(ButtonBehavior , Label) :
    pass

Window.size = (320, 600)


class Eventerly(MDApp) :
    def build(self):
        self.my_firebase = MyFirebase()
        files = Builder.load_file("main.kv")
        return files


    def change_screen(self , filename) :
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.current = filename
        pass

Eventerly().run()