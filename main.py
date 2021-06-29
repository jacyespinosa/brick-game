from turtle import Screen, Turtle
from bricks import Bricks
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

brick = Turtle()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)


add_brick = Bricks()
paddle = Paddle()
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(paddle.move_left, 'Left')
screen.onkey(paddle.move_right, 'Right')


is_game_over = False
def brick_game():
    speed = 0.1
    global is_game_over
    while not is_game_over:
        screen.update()
        time.sleep(speed)
        ball.move()

        if len(add_brick.bricks) == 0:
            score.win()
            score.reset()

        if paddle.xcor() > 230:
            paddle.goto(230, -280)

        if paddle.xcor() < -230:
            paddle.goto(-230, -280)

        if ball.xcor() > 280 or ball.xcor() < -280:
            ball.other_bounce()

        if ball.ycor() > 250:
            ball.bounce()

        if ball.ycor() < -280:
            speed = 0.1
            ball.goto(0, 0)
            ball.bounce()
            score.subtract_life()
            if score.lives == 0:
                score.reset()
                is_game_over = True

        if ball.distance(paddle) < 60 and ball.ycor() < -250:
           ball.bounce()


        for brick in add_brick.bricks:
            if ball.distance(brick) < 40:
                ball.bounce()
                speed *= 0.9
                brick.goto(1000, 1000)
                add_brick.bricks.remove(brick)
                score.add_point()


while len(add_brick.bricks) == 0:
    add_brick.create_bricks()

if is_game_over is False:
    brick_game()

screen.listen()
screen.exitonclick()