import turtle as trtl

painter = trtl.Turtle()
painter.pensize(5)

# draw body
painter.penup()
painter.goto(0, -20)
painter.pendown()
painter.pensize(100)
painter.circle(75, 360)
painter.goto(0,30)

# draw legs
painter.pensize(15)
painter.penup()
painter.goto(-95,135)
painter.left(160)
painter.pendown()

# left side
#30
x = 0
painter.left(30)
for i in range(4):
    painter.penup()
    painter.goto(-80,105)
    painter.right(5+10*x)
    painter.pendown()
    painter.forward(150)
    x += 1

# right side
#80
x=0 #Hein added this to reset your x since you start a new loop
#painter.left(80) #Hein found this unnecessary
for i in range(4):
    painter.pu()
    painter.goto(60,105)
    painter.setheading(-10 + 20*x)
    painter.pd()
    painter.forward(150)
    x += 1
    #Warlan's code below. Hein's is above
    '''
    painter.penup()
    painter.goto(60,105)
    #50
    painter.left(5+10*x)
    painter.pendown()
    painter.forward(150)
    x += 1
    '''

# head
painter.setheading(280) 
#Need to adjust the heading of the turtle because it is different when it finished the legs. THis will work
painter.penup()
painter.goto(-55,200)
painter.pendown()
painter.pensize(50)
painter.circle(50,360)
painter.pendown()
painter.goto(-5,200)
painter.pendown()
painter.forward(1)

# Face
painter.goto(-40,230)
painter.pensize(5)
painter.pencolor("white")
painter.circle(10,360)
painter.penup()
painter.goto(5,230)
painter.pendown()
painter.circle(10,360)

# Hat
painter.penup()
painter.goto(-70, 260)
painter.left(90)
painter.pendown()
painter.pencolor("red")
painter.pensize(20)
painter.forward(120)
painter.left(90)
painter.penup()
painter.forward(10)
painter.pendown()
painter.pensize(30)
painter.pencolor("black")
painter.circle(60,180)
painter.penup()
painter.backward(15)
painter.left(90)
painter.pendown()
painter.forward(100)
painter.left(120)
painter.forward(20)
painter.left(60)
painter.forward(50)
painter.penup()
painter.pensize(10)
painter.pencolor("red")
painter.goto(-35,280)
painter.right(120)
painter.pendown()
painter.forward(40)
painter.right(120)
painter.forward(40)
painter.backward(10)
painter.right(120)
painter.forward(20)

wn = trtl.Screen()
wn.mainloop()