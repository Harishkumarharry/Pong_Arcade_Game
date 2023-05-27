import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from dash import Dash

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong: The famous arcade game.")
screen.tracer(0)

r_paddle = Paddle((350, 0), "red")
l_paddle = Paddle((-350, 0), "green")
dash = Dash()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect collision with r_paddle and l_paddle.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    # Detect R paddle miss.
    if ball.xcor() > 380:
        ball.ball_reset()
        scoreboard.l_point()

    # Detect L paddle miss.
    if ball.xcor() < -380:
        ball.ball_reset()
        scoreboard.r_point()

screen.exitonclick()
