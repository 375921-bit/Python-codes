import turtle, time, random

delay = 0.1
score = 0

# Screen setup
s = turtle.Screen()
s.title("🐍 Snake Game")
s.bgcolor("black")
s.setup(600, 600)
s.tracer(0)

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("lime")
head.penup()
head.direction = "stop"

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Body + Score
body = []
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Courier", 18, "normal"))

# Controls
def go_up():    head.direction = "up" if head.direction != "down" else head.direction
def go_down():  head.direction = "down" if head.direction != "up" else head.direction
def go_left():  head.direction = "left" if head.direction != "right" else head.direction
def go_right(): head.direction = "right" if head.direction != "left" else head.direction
for k, f in zip(["w", "s", "a", "d"], [go_up, go_down, go_left, go_right]): s.onkeypress(f, k)
s.listen()

# Move
def move():
    x, y = head.xcor(), head.ycor()
    if head.direction == "up": head.sety(y + 20)
    if head.direction == "down": head.sety(y - 20)
    if head.direction == "left": head.setx(x - 20)
    if head.direction == "right": head.setx(x + 20)

# Game loop
while True:
    s.update()

    # Border collision
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for seg in body: seg.goto(1000, 1000)
        body.clear()
        score = 0
        pen.clear(); pen.write(f"Score: {score}", align="center", font=("Courier", 18, "normal"))

    # Eat food
    if head.distance(food) < 20:
        food.goto(random.randint(-290, 290), random.randint(-290, 290))
        seg = turtle.Turtle()
        seg.shape("square")
        seg.color("lime")
        seg.penup()
        body.append(seg)
        score += 10
        pen.clear(); pen.write(f"Score: {score}", align="center", font=("Courier", 18, "normal"))

    # Move body
    for i in range(len(body) - 1, 0, -1):
        body[i].goto(body[i-1].xcor(), body[i-1].ycor())
    if body:
        body[0].goto(head.xcor(), head.ycor())

    move()

    # Self collision
    for seg in body:
        if seg.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for seg in body: seg.goto(1000, 1000)
            body.clear()
            score = 0
            pen.clear(); pen.write(f"Score: {score}", align="center", font=("Courier", 18, "normal"))

    time.sleep(delay)