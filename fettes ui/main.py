#! /usr/bin/python
# main.py

from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, StringProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line, Canvas
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class BoxyFoxy(BoxLayout):
	nameinput=ObjectProperty(None)
	submitbutton=ObjectProperty(None)

class Controller(FloatLayout):
	boxy=ObjectProperty(None)
	def __init__(self):
		FloatLayout.__init__(self)
		self.boxy.submitbutton.bind(on_press = self.submit_data)
	def submit_data(self,event):
		self.clear_widgets()
		self.add_widget(Label(pos_hint = {'center_x' : .5, 'center_y' : .5},text='thanks '+ self.boxy.nameinput.text,font_size=100))	

class UIApp(App):
	def build(self):
		root = Controller()
		return root
		
if __name__ == '__main__':
	UIApp().run()
		