#Snake_4.py

import turtle
import random
import time

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

snake_head = turtle.Turtle("square")
snake_head.color("green")
snake_head.penup()
snake_head.goto(0, 0)
snake_direction = "Stop"

food = turtle.Turtle("circle")
food.color("red")
food.penup()
food.goto(0, 100)

snake_body = []

def move_snake():
        if snake_direction == "Up": snake_head.sety(snake_head.ycor() + 20)
        if snake_direction == "Down": snake_head.sety(snake_head.ycor() - 20)
        if snake_direction == "Left": snake_head.setx(snake_head.xcor() - 20)
        if snake_direction == "Right": snake_head.setx(snake_head.xcor() + 20)

import sys
def go_up():
    global snake_direction
    snake_direction = "Up"

def go_down():
    global snake_direction
    snake_direction = "Down"

def go_left():
    global snake_direction
    snake_direction = "Left"

def go_right():
    global snake_direction
    snake_direction = "Right"

screen.listen()

screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_left, "a")
screen.onkey(go_right, "d")

score = 0
game_running = True

while game_running:
    screen.update()

    # Wall collision
    if abs(snake_head.xcor()) > WALL_LIMIT or abs(snake_head.ycor()) > WALL_LIMIT:
        break

    # Food collision
    if snake_head.distance(food) < FOOD_DISTANCE:
        # Move food to a new random spot
        new_x = random.randint(-280, 280)
        new_y = random.randint(-280, 280)
        food.goto(new_x, new_y)

        # Add new body segment
        segment = turtle.Turtle("square")
        segment.color("lightgreen")
        segment.penup()
        body_segments.append(segment)

        score += 10   # Just for fun. Maybe add a scoreboard later.

    # Move body segments (from last to first)
    for i in range(len(body_segments) - 1, 0, -1):
        body_segments[i].goto(body_segments[i - 1].pos())

    # First body segment follows the head
    if body_segments:
        body_segments[0].goto(snake_head.pos())

    # Move snake head last
    move_snake()

    # Collision with own body
    for segment in body_segments:
        if segment.distance(snake_head) < 10:
            game_running = False

    time.sleep(0.1)

# ---- End of game ----
turtle.done()