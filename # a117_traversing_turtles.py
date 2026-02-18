#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle"]
# When a color is deleted, the color 2nd to last of the removed color starts the design
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]


for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)
'''
for c in turtle_colors:
  t = trtl.Turtle(color=c)
  my_turtles.append(t)
'''

#  Origin 
startx = 0
starty = 0

# Moves
x = 0
for t in my_turtles:
  t.penup()
  t.goto(startx, starty)
  t.pendown()
  color = turtle_colors.pop()
  t.pencolor(color)
  t.fillcolor(color)
  t.right(45*x)     
  t.forward(50)


#	New starting point
  startx = t.xcor()
  starty = t.ycor()
  x += 1


wn = trtl.Screen()
wn.mainloop()