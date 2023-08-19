# Bike App Android Ver 1.0
import kivy
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class WindowManager(ScreenManager):
    pass

class HomeWindow(Screen):
    pass

class BikenameScreen(Screen):
    def on_save(self):
        motorname = self.ids.motorname.text
        if motorname:
            root = self.parent
            root.add_widget(CcScreen(name="ccinput"))
            root.current = "ccinput"

class CcScreen(Screen):
    pass

class HpScreen(Screen):
    pass

class BikeweightScreen(Screen):
    pass

class UserweightScreen(Screen):
    pass

class CompanionweightScreen(Screen):
    pass

class MaxVelocityScreen(Screen):
    pass


class bikeapp(App):
    pass
    
bikeapp().run()