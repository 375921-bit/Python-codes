#   a116_buggy_image.py
import turtle as trtl

# Creating the spider
painter = trtl.Turtle()
painter.pensize(40)
painter.circle(20)

# amount of legs
legs = 8

# leg length
length = 150

# spacing between the legs
z = 360 / legs

painter.pensize(5)
# legs removed
removed = 0
while (removed < legs):
  if removed < 4:
    painter.goto(0,20)
    painter.setheading(30*removed-50)
    painter.forward(length)
    removed = removed + 1
  else:
    painter.goto(0,20)
    painter.setheading(30*removed+20)
    painter.forward(length)
    removed = removed + 1

painter.pensize(10)
painter.color("dark red")
painter.penup()
painter.goto(-20,40)
painter.pendown()
painter.circle(5)
painter.penup()
painter.goto(10,40)
painter.pendown()
painter.circle(5)
painter.penup()
painter.goto(-24,55)
painter.right(230)
painter.pendown()
painter.color("red")
painter.pensize(15)
painter.forward(45)
painter.penup()
painter.goto(24,68)
painter.left(90)
painter.color("black")
painter.pensize(15)
painter.pendown()
painter.circle(25, 180)
painter.goto(-20, 65)
painter.left(90)
painter.forward(35)
painter.left(90)
painter.circle(15,180)
painter.pensize(5)
painter.color("white")
painter.left(160)
painter.forward(20)
painter.right(70)
painter.forward(5)
painter.right(50)
painter.forward(25)
painter.penup()
painter.goto(-9,73)
painter.pendown()
painter.left(50)
painter.forward(15)


painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()
