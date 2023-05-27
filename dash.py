from turtle import Turtle


class Dash(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.pensize(5)
        self.penup()
        self.goto(0, -300)
        self.setheading(90)
        self.pendown()
        self.draw_line()

    def draw_line(self):
        # pass
        for _ in range(30):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
