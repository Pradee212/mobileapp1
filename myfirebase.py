import pyrebase
from firebase import firebase
import json
from kivymd.app import MDApp

config = {
    "apiKey": "AIzaSyDdeGrr84z-zwCFR23HXVAjpd322v1HIsY",
    "authDomain": "eventerly-84a0a.firebaseapp.com",
    "databaseURL": "https://eventerly-84a0a-default-rtdb.firebaseio.com",
    "projectId": "eventerly-84a0a",
    "storageBucket": "eventerly-84a0a.appspot.com",
    "messagingSenderId": "374097608414",
    "appId": "1:374097608414:web:976283df3546ae6b778c4f",
    "measurementId": "G-8G09328VJY"
}

firebase_auth = pyrebase.initialize_app(config)
firebase_data = firebase.FirebaseApplication("https://eventerly-84a0a-default-rtdb.firebaseio.com/" , None)

class MyFirebase() :
    def sign_up(self , username , email , password):

        try :
            # RealTime Database
            data = {
                "UserName": username,
                "Email": email,
                "Password": password
            }
            result = firebase_data.post("user data", data)

            # Creating User
            signup_auth = firebase_auth.auth()
            user_signup = signup_auth.create_user_with_email_and_password(email, password)
            print("SignUp Successfully")
            MDApp.get_running_app().root.ids["signup_screen"].ids["signup_screen"].text = "[b][color=#FF0000]Signup Succesfully.[/color][/b]"
        except:
            MDApp.get_running_app().root.ids["signup_screen"].ids["signup_screen"].text = "[b][color=#0000FF]Please enter correct details.[/color][/b]"




    def sign_in(self , email , password):
        signin_auth = firebase_auth.auth()


        try :
            user_login = signin_auth.sign_in_with_email_and_password(email,password)
            print("Login Successfully !!!")
            print(user_login["registered"])
            path_to_home = user_login["registered"]

            if path_to_home == True :
                print("hello")
                MDApp.get_running_app().root.ids["login_screen"].ids["login_message"].text = ""
                MDApp.get_running_app().change_screen("home_screen")
                MDApp.get_running_app().root.ids["home_screen"].ids["passing_email"].text = "[b]%s[/b]" %email

        except :
            MDApp.get_running_app().root.ids["login_screen"].ids["login_message"].text = "[b]Invalid Email or Password[/b]"

    def forgot_password(self , email) :
        try:
            auth = firebase_auth.auth()
            auth.send_password_reset_email(email)
            MDApp.get_running_app().root.ids["forgot_password_screen"].ids["forgot_message"].text = "[b]Thanks! Please check your email .[/b]"
        except:
            MDApp.get_running_app().root.ids["forgot_password_screen"].ids["forgot_message"].text = "[b][color=#FF0000]Please Enter Correct Email !.[/color][/b]"
