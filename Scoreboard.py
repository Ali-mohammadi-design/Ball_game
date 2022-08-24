from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.score=0
        self.write(arg=f"Score={self.score}", move=True, align='left', font=('Arial', 8, 'normal'))

    def score_growing(self):
        self.clear()
        self.score=self.score+1
        self.goto(0, 260)
        self.write(arg=f"Score={self.score}", move=True, align='left', font=('Arial', 8, 'normal'))
    def score_decreasing(self):
        self.clear()
        self.score=self.score-1
        self.goto(0, 260)
        self.write(arg=f"Score={self.score}", move=True, align='left', font=('Arial', 8, 'normal'))