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

class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()

        #bounce of paddles
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        #bounce ball off bottom or top
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        #went of to a side to score point?
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y

class Show_details(BoxLayout):
	def __init__(self,name1,name2):
		BoxLayout.__init__(self)
		self.color=(1,0,0,1)
		self.padding=10
		self.spacing=10
		self.orientation='vertical'
		self.pos_hint={'center_x':.5,'center_y':.5}
		self.size_hint=(.5,.5)
		self.add_widget(Label(text='Player 1: '+ name1,size_hint=(.5,.5),pos_hint={'center_x':.5,'center_y':.5}))
		self.add_widget(Label(text='Player 2: '+ name2,size_hint=(.5,.5),pos_hint={'center_x':.5,'center_y':.5}))

class Text_input(BoxLayout):
	def __init__(self):
		BoxLayout.__init__(self)
		self.background_color=(1,0,0,1)
		self.padding=10
		self.spacing=10
		self.orientation='vertical'
		self.pos_hint={'center_x':.5,'center_y':.5}
		self.size_hint=(.5,.5)
		self.nameinput=TextInput(pos_hint={'center_x':.5,'center_y':.5},size_hint=(.5,.5),multiline=False)
		self.nameinput2=TextInput(pos_hint={'center_x':.5,'center_y':.5},size_hint=(.5,.5),multiline=False)
		self.subscribebutton=Button(text='Subscribe',pos_hint={'center_x':.5,'center_y':.5},size_hint=(.5,.5))
		self.add_widget(Label(text='Player 1: Name',size_hint=(.5,.5),pos_hint={'center_x':.5,'center_y':.5}))
		self.add_widget(self.nameinput)
		self.add_widget(Label(text='Player 2: Name',size_hint=(.5,.5),pos_hint={'center_x':.5,'center_y':.5}))
		self.add_widget(self.nameinput2)
		self.add_widget(Label(text=''))
		self.add_widget(self.subscribebutton)

class Top_button_bar(BoxLayout):
	def __init__(self):
		BoxLayout.__init__(self)
		self.pos_hint={'center_x':.5,'center_y':.9}
		self.size_hint=(0.9,0.1)
		self.sub=Button(text='Sign in')
		self.show=Button(text='Show details')
		self.play=Button(text='Play')
		self.add_widget(self.sub)
		self.add_widget(self.show)
		self.add_widget(self.play)
		
class Controller(FloatLayout):
	player1=''
	player2=''
	def add_bar(self):
		self.bar=Top_button_bar()
		self.add_widget(self.bar)
		self.bar.sub.bind(on_press = self.add_ti)
		self.bar.show.bind(on_press = self.add_details)
		self.bar.play.bind(on_press = self.game)
	def game(self, event):
		self.clear_widgets()		
		game = PongGame()
		game.serve_ball()
		Clock.schedule_interval(game.update, 1.0 / 60.0)
		self.add_widget(game)
		exit=Button(text='exit',size_hint=(.05,.05))
		self.add_widget(exit)
		exit.bind(on_press=self.add_details)
	def add_details(self,event=0):
		self.clear_widgets()
		self.add_bar()
		self.details=Show_details(self.player1,self.player2)
		self.add_widget(self.details)
	def add_ti(self,event=0):
		self.clear_widgets()
		self.add_bar()
		self.ti=Text_input()
		self.add_widget(self.ti)
		self.ti.subscribebutton.bind(on_press = self.submit_data)
	def __init__(self):
		FloatLayout.__init__(self)
		self.add_bar()
		self.add_ti()
	def submit_data(self,event):
		self.player1=self.ti.nameinput.text
		self.player2=self.ti.nameinput2.text
		self.clear_widgets()
		self.add_bar()
		self.add_widget(Label(pos_hint = {'center_x' : .5, 'center_y' : .5},text='Super, danke!',font_size=30))	

class UiApp(App):
	def build(self):
		root = Controller()
		return root
		
if __name__ == '__main__':
	UiApp().run()
		