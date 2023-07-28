from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
from time import sleep

PLAYER1_START = -350
PLAYER2_START = 350

screen = Screen()
user1_paddle = Paddle()
user2_paddle = Paddle()
scoreboard = Scoreboard()
ball = Ball()

user1_paddle.create_paddle(PLAYER1_START)
user2_paddle.create_paddle(PLAYER2_START)

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.listen()
screen.onkey(user1_paddle.up, "w")
screen.onkey(user1_paddle.down, "s")
screen.onkey(user2_paddle.up2, "Up")
screen.onkey(user2_paddle.down2, "Down")


game_is_on = True
while game_is_on:

    ball.forward(4)

    if ball.distance(user1_paddle) < 50 and ball.xcor() < -330 or ball.distance(user2_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_vertical()

    if ball.xcor() > 390:
        scoreboard.add_point1()
        ball.refresh()
        sleep(2)

    if ball.xcor() < -390:
        scoreboard.add_point2()
        ball.refresh()
        sleep(2)

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_horizontal()

    if scoreboard.score1 == 5:
        game_is_on = False
        scoreboard.user1_win()

    elif scoreboard.score2 == 5:
        game_is_on = False
        scoreboard.user2_win()

screen.exitonclick()
