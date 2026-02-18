#Drawing_activity

import turtle as trtl
painter = trtl.Turtle()

painter.goto(0,100)
painter.circle(80,360)
painter.penup()
painter.goto(-50,0)
painter.pendown()
painter.forward(100)
painter.penup()
painter.goto(-90,260)
painter.pendown()
painter.forward(200)
painter.left(90)
painter.forward(50)
painter.left(90)
painter.forward(25)
painter.right(90)
painter.forward(50)


wn = trtl.Screen()
wn.mainloop()