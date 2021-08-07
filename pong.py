import turtle
import os

win = turtle.Screen()
win.title("Pong by The Man in Black")
win.bgcolor("red")
win.setup(width=666, height=666)
win.tracer(0)


# Main Loop
while True:
    win.update()