from turtle import Turtle
import random

COLORS = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')


class Bricks:
    def __init__(self):
        self.bricks = []

    def create_bricks(self):
        y = 240
        i = 0
        while y > 100:
            for x in range(-250, 250, 83):
                brick = Turtle()
                brick.penup()
                brick.shape('square')
                brick.shapesize(stretch_wid=1, stretch_len=4)
                brick.color(random.choice(COLORS))
                brick.goto((x, y))
                self.bricks.append(brick)
                i += 1
            y -= 30

