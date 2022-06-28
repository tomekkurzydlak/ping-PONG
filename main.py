from turtle import Screen
from game import Paddle, Ball, Scoreboard, Worker
import time

is_playing = True

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping PONG")

r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
ball = Ball()
worker = Worker()
worker.draw_board()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

scoreboard = Scoreboard()

while is_playing:

    time.sleep(ball.starting_speed)
    screen.update()
    ball.move()

    #top and bottom bounce
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    #paddles collide
    if ball.xcor() > 330 and ball.distance(r_paddle) < 50 or ball.xcor() < -330 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    #right paddle misses
    if ball.xcor() > 390:
        ball.new_game()
        scoreboard.l_point()

    #left paddle misses
    if ball.xcor() < -390:
        ball.new_game()
        scoreboard.r_point()

screen.exitonclick()
