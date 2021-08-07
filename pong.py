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

paddle_two = turtle.Turtle()
paddle_two.speed(0)
paddle_two.shape("square")
paddle_two.color("white")
paddle_two.shapesize(stretch_wid=5, stretch_len=1)
paddle_two.penup()
paddle_two.goto(290, 0)

# Ball

pong = turtle.Turtle()
pong.speed(0)
pong.shape("square")
pong.color("white")
pong.penup()
pong.goto(0, 0)

# Functionality

def paddle_one_up():
    y = paddle_one.ycor()
    y += 20
    paddle_one.sety(y)

def paddle_one_dwn():
    y = paddle_one.ycor()
    y -= 20
    paddle_one.sety(y)

# Keyboard Binding

win.listen()
win.onkeypress(paddle_one_up, "w")
win.onkeypress(paddle_one_dwn, "s")
# Main Loop
while True:
    win.update()

