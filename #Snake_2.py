#Snake

import turtle
painter = turtle.Turtle()
import random
rand = random.Random()
import json
import os
import time

# Load leaderboard
leaderboard_file = "leaderboard.json"
leaderboard = json.load(open(leaderboard_file)) if os.path.exists(leaderboard_file) else []

# Set up screen
screen = painter.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

# Create snake head
head = painter("square")
head.color("green")
head.penup()
head.goto(0, 0)
direction = "Stop"

# Create food
food = painter("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# List for snake segments
segments = []

def move():
    if direction == "Up": head.sety(head.ycor() + 20)
    elif direction == "Down": head.sety(head.ycor() - 20)
    elif direction == "Left": head.setx(head.xcor() - 20)
    elif direction == "Right": head.setx(head.xcor() + 20)

import sys
# Direction controls
screen.listen()
screen.onkey(lambda: setattr(sys.modules[__name__], 'direction', "Up"), "w")
screen.onkey(lambda: setattr(sys.modules[__name__], 'direction', "Down"), "s")
screen.onkey(lambda: setattr(sys.modules[__name__], 'direction', "Left"), "a")
screen.onkey(lambda: setattr(sys.modules[__name__], 'direction', "Right"), "d")

score = 0
game_over = False

while not game_over:
    screen.update()
    # Check wall collision
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        break
    # Check food collision
    if head.distance(food) < 15:
        food.goto(rand.randint(-280, 280), rand.randint(-280, 280))
        new_segment = painter("square")
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
    # Check self collision
    if any(segment.distance(head) < 10 for segment in segments):
        break
    time.sleep(0.1)

# Save score and show leaderboard
name = painter.textinput("Game Over", "Name?")
if name:
    leaderboard.append({"name": name, "score": score})
    leaderboard = sorted(leaderboard, key=lambda x: x['score'], reverse=True)[:5]
    json.dump(leaderboard, open(leaderboard_file, "w"))

# Display leaderboard
screen.clearscreen()
display = painter()
display.hideturtle()
display.penup()

display.goto(0, 250)
display.write("Leaderboard", align="center", font=("Arial", 20, "bold"))
y_pos = 220
for entry in leaderboard:
    display.goto(0, y_pos)
    display.write(f"{entry['name']} {entry['score']}", align="center", font=("Arial", 14))
    y_pos -= 20

turtle.done()