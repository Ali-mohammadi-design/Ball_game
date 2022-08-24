import random
from turtle import Turtle
from random import randint
import time
class Ball (Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.resizemode("user")
        self.left(90)
        self.shapesize(1, 1, 1)
        self.goto(0,0)
        self.step_x=2
        self.step_y=2
        self.speed=0.02

    def bounce(self):
        y = self.ycor()
        if y>280 or y<-280:
         self.step_y=self.step_y*-1

    def bounce_paddle(self):
        self.step_y=self.step_y+random.randint(0,1)
        self.step_y = self.step_y * -1
        self.step_x = self.step_x * -1
    def move(self):
            x = self.xcor() + self.step_x
            y = self.ycor() +self.step_y
            time.sleep(self.speed)
            self.goto(x, y)
    def start_from_zero_position(self):
        self.goto(0, 0)

    def ball_speed(self,score):
        if score%3==0 and score>1:
            self.speed=self.speed - 0.0005
        if self.speed<=0:
            self.speed=0

    def collision(self):
        y=self.ycor()
        if y>200:
            rotate=random.randint(0,45)
            self.left(rotate)

