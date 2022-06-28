from turtle import Turtle

class Worker(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.hideturtle()
        self.color("white")
    def draw_board(self):
        self.penup()
        self.goto(0, 300)
        self.pendown()
        self.goto(0, -300)

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.starting_speed = 0.08
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.starting_speed *= 0.9

    def new_game(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.starting_speed = 0.08

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.print_score()

    def print_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.print_score()

    def r_point(self):
        self.r_score += 1
        self.print_score()