import turtle as painter
import random as rand
import json
import os as operating_system
import time

leaderboard_file = "leaderboard.json"
leaderboard = json.load(open(leaderboard_file)) if operating_system.path.exists(leaderboard_file) else []

screen = painter.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

draw_boundary = 600
painter.hideturtle()
painter.color("White")
painter.penup()
def draw_boundary(perimeter):
    painter.goto(-perimeter/2,perimeter/2)
    painter.pendown()
    for length in range(4):
        painter.forward(perimeter)
        painter.right(90)
draw_boundary(600)

head = painter.Turtle("square")
head.color("green")
head.penup()
head.goto(0, 0)
direction = "Stop"

food = painter.Turtle("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

def move():
    if direction == "Up": head.sety(head.ycor() + 20)
    if direction == "Down": head.sety(head.ycor() - 20)
    if direction == "Left": head.setx(head.xcor() - 20)
    if direction == "Right": head.setx(head.xcor() + 20)

import sys

screen.listen()
screen.onkey(lambda: setattr(sys.modules[__name__], 'direction', "Up"), "w")
screen.onkey(lambda: setattr(sys.modules[__name__], 'direction', "Down"), "s")
screen.onkey(lambda: setattr(sys.modules[__name__], 'direction', "Left"), "a")
screen.onkey(lambda: setattr(sys.modules[__name__], 'direction', "Right"), "d")

score = 0
game_over = False

while not game_over:
    screen.update()

    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        break

    if head.distance(food) < 15:
        food.goto(rand.randint(-280, 280), rand.randint(-280, 280))
        new_segment = painter.Turtle("square")
        new_segment.color("lightgreen")
        new_segment.penup()
        segments.append(new_segment)
        score += 10
    # Move segments
    for i in range(len(segments) - 1, 0, -1):
        segments[i].goto(segments[i-1].position())
    if segments:
        segments[0].goto(head.position())
    move()

    if any(segment.distance(head) < 10 for segment in segments):
        break
    time.sleep(0.1)

name = painter.textinput("Game Over", "Name?")
if name:
    leaderboard.append({"name": name, "score": score})
    leaderboard = sorted(leaderboard, key=lambda x: x['score'], reverse=True)[:5]
    json.dump(leaderboard, open(leaderboard_file, "w"))

screen.clearscreen()
display = painter.Turtle()
display.hideturtle()
display.penup()

display.goto(0, 250)
display.write("Leaderboard", align="center", font=("Arial", 20, "bold"))
y_pos = 220
for entry in leaderboard:
    display.goto(0, y_pos)
    display.write(f"{entry['name']} {entry['score']}", align="center", font=("Arial", 14))
    y_pos -= 20

wn = painter.Screen()
wn.mainloop()