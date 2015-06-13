#! /usr/bin/python
# main.py


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, StringProperty
from kivy.vector import Vector
from kivy.clock import Clock



class PayButton(Widget):
    labeltext = StringProperty("Pay 100$")
class BH(Widget):
    pay = ObjectProperty(None)


    def main(self):
        print "lol"


    def update(self, dt):
            return



class BHApp(App):
    def build(self):
        app = BH()
        app.main()
        Clock.schedule_interval(app.update, 1.0 / 60.0)
        return app

if(__name__ == "__main__"):
    BHApp().run()
