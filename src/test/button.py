#! /usr/bin/python
# main.py


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, StringProperty
from kivy.vector import Vector
from kivy.clock import Clock

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button



class ButtonApp(App):
    def build(self):
        root = FloatLayout()
        b1 = Button(pos_hint = {'x' : 0, 'center_y' : 0.5}, text= "Launch Missile")
        b2 = Button(pos_hint = {'left' : 0, 'top' : 0}, text="Back")
        root.add_widget(b1)
        root.add_widget(b2)
        return root

if(__name__ == "__main__"):
    ButtonApp().run()
