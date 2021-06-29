from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.lives = 3
        self.color('white')
        self.hideturtle()
        self.write_score()
        self.write_life()

    def write_score(self):
        self.penup()
        self.setposition(x= 90, y=280)
        self.pendown()
        self.write("SCORE: {}                        HIGH SCORE: {}".format(self.score, self.high_score),
                   align="center", font=("Times New Roman", 20, "normal"))

    def add_point(self):
        self.score += 1
        self.clear()
        self.write_score()
        self.write_life()

    def write_life(self):
        self.penup()
        self.setposition(x= -250, y=280)
        self.pendown()
        self.write("LIVES: {}".format(self.lives), align="center", font=("Times New Roman", 20, "normal"))

    def subtract_life(self):
        self.lives -= 1
        self.clear()
        self.write_score()
        self.write_life()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.write_score()
        self.gameover()

    def gameover(self):
       self.penup()
       self.setposition(x=0, y= -50)
       self.pendown()
       self.write("GAME OVER!!!", align="center", font=("Times New Roman", 50, "normal"))

    def win(self):
        self.penup()
        self.setposition(x=0, y= -50)
        self.pendown()
        self.write("CONGRATULATIONS!!!", align="center", font=("Times New Roman", 50, "normal"))