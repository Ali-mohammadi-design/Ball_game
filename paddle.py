from turtle import Turtle
import time
class Paddle(Turtle):
    def __init__(self):
        super().__init__()


    def make(self,position):
            self.color("white")
            self.shape("square")
            self.penup()
            self.resizemode("user")
            self.left(90)
            self.shapesize(1, 10, 1)
            self.goto(position, 0)
            self.step=8
    def speed_increase(self):
        self.step=self.step+1

    def speed_decrease(self):
        self.step = self.step - 1

    def move (self):
        y=self.ycor()+self.step
        self.goto(300,y)
        if y>190 or y<-190:
            self.step=self.step*-1

