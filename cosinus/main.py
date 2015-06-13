#! /usr/bin/python
# main.py


from math import cos, sin

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, StringProperty
from kivy.vector import Vector
from kivy.clock import Clock

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.clock import time

class Controller(Widget):
    movingButton = ObjectProperty(None)
    
    def update(self, dt):
        self.movingButton.x = self.width * cos(time.time())
        self.movingButton.y = self.height * sin(time.time())

class CosinusApp(App):
    def build(self):
        root = Controller()
        Clock.schedule_interval(root.update, 1.0 / 60.0)
        return root



if(__name__ == "__main__"):
    CosinusApp().run()



