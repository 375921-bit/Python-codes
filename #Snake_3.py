import turtle
import random
import time

#Ask user to play game
answer = input("Would you like to play a game?")
while answer == "No":
    answer = input("Would you like to play a game?")
if answer == "Yes":
   
    #Ask info
    speed = float(input("Enter a speed: "))

    movement = float(input("Enter the movement: "))
   
    steps = int(input("Enter the number of steps: "))

    mode = input("Enter the mode(easy ore normal): ")

    #Setup the screen
    screen = turtle.Screen()
    screen.setup(600,600)
    screen.bgcolor("black")
    screen.tracer(0)
   
    #Make the snake
    player = turtle.Turtle("square")
    player.color("green")
    player.penup()
    player.goto(0,0)
    snake_direction = "Stop"
   
    #Make the food
    food = turtle.Turtle("circle")
    food.color("red")
    food.penup()
    food.goto(0,100)
   
    #Create the movement
    def move_snake(movement, steps):
        for i in range(steps):
            if mode == "easy":
                x, y = player.xcor(), player.ycor()
                if snake_direction == "Up":
                    player.sety(y + 0.5 * movement)
                elif snake_direction == "Down":
                    player.sety(y - 0.5 * movement)
                elif snake_direction == "Left":
                    player.setx(x - 0.5 * movement)
                elif snake_direction == "Right":
                    player.setx(x + 0.5 * movement)

            elif mode == "normal":
                x, y = player.xcor(), player.ycor()
                if snake_direction == "Up":
                    player.sety(y + movement)
                elif snake_direction == "Down":
                    player.sety(y - movement)
                elif snake_direction == "Left":
                    player.setx(x - movement)
                elif snake_direction == "Right":
                    player.setx(x + movement)
            
#Up down left right
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
   
    #Make and keep the tail
    tail = []
    game_over = False
    while not game_over:
        screen.update()
       
        if abs(player.xcor()) > 290 or abs(player.ycor()) > 290:
            break
       
        if player.distance(food) < 15:
            food.goto(random.randint(-280,280), random.randint(-280,280))
            new_tail = turtle.Turtle("square")
            new_tail.color("green")
            new_tail.penup()
            tail.append(new_tail)
       
        #Move tail
        for i in range(len(tail) -1,0,-1):
            tail[i].goto(tail[i-1].position())
        if tail:
            tail[0].goto(player.position())
        move_snake(movement,steps)
       
        if any(segment.distance(player) < 10 for segment in tail):
            break
       
        time.sleep(speed)
       
#Keep screen on
wn = turtle.Screen()
wn.mainloop()