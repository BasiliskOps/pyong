import turtle
import os

win = turtle.Screen()
win.title("Pong by The Man in Black")
win.bgcolor("red")
win.setup(width=666, height=666)
win.tracer(0)


# Paddle One
paddle_one = turtle.Turtle()
paddle_one.speed(0)
paddle_one.shape("square")
paddle_one.color("white")
paddle_one.shapesize(stretch_wid=5, stretch_len=1)
paddle_one.penup()
paddle_one.goto(-300, 0)


# Paddle Two



# Ball



# Main Loop
while True:
    win.update()
