# a124_maze_spiral_ws.py

import turtle
import random

# Set up turtle and screen
wn = turtle.Screen()
wn.bgcolor("black")
painter = turtle.Turtle()

painter.speed(5)

painter.color("light blue")
painter.pencolor("red")
painter.turtlesize(5)
wall_length = 10

def opening():
    painter.penup()
    painter.forward(10)
    painter.pendown()

# Draw the spiral maze
for i in range(48):
    amount = random.randint(0, wall_length)
    while amount > wall_length - 10:
        amount = random.randint(0, wall_length)
    
    amount_2 = random.randint(0,amount)
    painter.forward(amount_2)
# Make a door
    painter.left(90)
    painter.forward
    painter.back
    painter.right(90)
    painter.forward(amount - amount_2)
    opening()
    painter.forward(wall_length - amount - 10)
    painter.left(90)
    wall_length += 15

# Prepare turtle for movement
painter.turtlesize(1)
painter.shape("turtle")
painter.penup()
painter.goto(-10, 0)

# Movement functions
def move_up():
    painter.setheading(90)
    painter.forward(10)

def move_down():
    painter.setheading(270)
    painter.forward(10)

def move_left():
    painter.setheading(180)
    painter.forward(10)

def move_right():
    painter.setheading(0)
    painter.forward(10)

# Keyboard bindings
wn.listen()
wn.onkeypress(move_up, "w")
wn.onkeypress(move_down, "s")
wn.onkeypress(move_left, "a")
wn.onkeypress(move_right, "d")

wn.mainloop()