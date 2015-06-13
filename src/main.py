#! /usr/bin/python
# main.py


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

class BH(Widget):
    def main(self):
        print "lol"


class BHApp(App):
    def build(self):
        app = BH()
        app.main()
        return app

if(__name__ == "__main__"):
    BHApp().run()
