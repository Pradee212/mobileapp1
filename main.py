from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.label import Label
from kivymd.uix.pickers import MDDatePicker, MDTimePicker

from myfirebase import MyFirebase
from kivy.core.window import Window

class HomeScreen(Screen) :
    pass
class FirstScreen(Screen) :
    pass
class SettingsScreen(Screen) :
    pass
class EventScreen(Screen) :
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

    def get_date(self, instance, value, date_range):
        self.root.ids["home_screen"].ids["date_label"].text = str(value)

    def on_date_cancel(self, instance, value):
        self.root.ids["home_screen"].ids["date_label"].text = "You clicked cancel!"

    def show_date_picker(self):
        date_dialog = MDDatePicker()

        date_dialog.bind(on_save=self.get_date, on_cancel=self.on_date_cancel)
        date_dialog.open()

    def get_time(self, instance, time):
        self.root.ids["home_screen"].ids["time_label"].text = str(time)

    def on_time_cancel(self, instance, time):
        self.root.ids["home_screen"].ids["time_label"].text = "You clicked cancel!"

    def show_time_picker(self):
        time_dialog = MDTimePicker()

        time_dialog.bind(on_cancel=self.on_time_cancel, time=self.get_time)
        time_dialog.open()

if __name__ == "__main__":
    Eventerly().run()