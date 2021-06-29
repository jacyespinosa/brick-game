from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.color('white')
        self.penup()
        self.goto(0, -280)

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())
        self.speed('fastest')

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
        self.speed('fastest')