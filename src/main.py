#! /usr/bin/python
# main.py


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, StringProperty
from kivy.vector import Vector
from kivy.clock import Clock



class PayButton(Widget):
	pass
class Bh(Widget):
    pay = ObjectProperty(None)



class BHApp(App):
    def build(self):
        app = Bh()
        return app

if(__name__ == "__main__"):
    BHApp().run()
