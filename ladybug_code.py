import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(45)
ladybug.circle(5)

# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -15
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
for Ladybug in range(2):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  xpos = ypos + 40
  ypos = xpos - 15
  num_dot = num_dots + 1

# amount of legs
legs = 6

# leg length
length = 59

# spacing between the legs
z = 360 / legs

ladybug.pensize(5)
ladybug.penup()
ladybug.left(100)
ladybug.goto(30,-10)
ladybug.pendown()
ladybug.forward(20)
ladybug.penup()
ladybug.goto(35,-30)
ladybug.pendown()
ladybug.forward(20)
ladybug.penup()
ladybug.goto(35,-50)
ladybug.pendown()
ladybug.forward(20)
ladybug.penup()
ladybug.left(160)
ladybug.goto(-30,-10)
ladybug.pendown()
ladybug.forward(20)
ladybug.penup()
ladybug.goto(-35,-30)
ladybug.pendown()
ladybug.forward(20)
ladybug.penup()
ladybug.goto(-35,-50)
ladybug.pendown()
ladybug.forward(20)
ladybug.penup()

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()