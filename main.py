from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong Game")
screen.tracer(0)

score = Scoreboard()

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

game_is_on = True
while game_is_on:
    time.sleep(0.09)
    screen.update()

    ball.move()
    if ball.ycor() >280 or ball.ycor()<-280:  # collision with up and down wall
        ball.bounce_y()
    #collision with right left paddle
    if ball.distance(r_paddle)<50 and ball.xcor() >320 or ball.distance(l_paddle)<50 and ball.xcor() <-320:
        print("collide")
        ball.bounce_x()

    if ball.xcor()>380:
        print("game over")
        ball.reset_ball()
        score.l_point()

    if ball.xcor()<-380:
       print("game over")
       ball.reset_ball()
       score.r_point()

screen.exitonclick()
