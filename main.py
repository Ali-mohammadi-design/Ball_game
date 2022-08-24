from turtle import Screen, Turtle
from paddle import Paddle
from Scoreboard import Scoreboard
from ball import Ball
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Game")
# timy=Turtle()
# timy.color("white")
screen.listen()
def up():
 paddle.forward(20)
def down():
    paddle.backward(20)
def up_s():
 paddle_s.forward(20)
def down_s():
    paddle_s.backward(20)
screen.onkey(up,"Up")
screen.onkey(down,"Down")
screen.onkey(up_s,"Right")
screen.onkey(down_s,"Left")
# first paddle
paddle=Paddle()
screen.tracer(0)
paddle.make(-300)

#second paddle
paddle_s=Paddle()
paddle_s.make(300)
screen.tracer(1)

ball=Ball()
screen.tracer(0)
scoreboard=Scoreboard()
game_is_on=True
score=0
while game_is_on:
    ball.bounce()
    ball.move()
    paddle_s.move()
    screen.update()
    print(ball.distance(paddle))
    ba= ball.xcor()
    if ball.distance(paddle)<90 and ba<-280 and ba>-304:
        ball.bounce_paddle()
    if ball.distance(paddle_s) < 90 and ba > 280 and ba<304:
        ball.bounce_paddle()
    if ba>400:
        scoreboard.score_growing()
        ball.start_from_zero_position()
        ball.bounce_paddle()
        score=score+1
        ball.ball_speed(score)
        paddle_s.speed_increase()
    if ba < -400:
        scoreboard.score_decreasing()
        ball.start_from_zero_position()
        ball.bounce_paddle()
        score=score-1
        paddle_s.speed_decrease()


















screen.exitonclick()