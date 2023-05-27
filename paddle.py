from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, paddle_position, paddle_color):
        super().__init__()
        self.shape("square")
        self.color(paddle_color)
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1, outline=12)
        self.goto(paddle_position)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

