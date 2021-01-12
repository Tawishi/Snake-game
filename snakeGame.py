import turtle
import time
import random

delay = 0.1

#set up the screen
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("green")
window.setup(width=600, height=600)
window.tracer(0) #turns off animation on the screen

# snake-head
head = turtle.Turtle()
head.speed(0) #animation speed of turtle module
head.shape("square")
head.color("black") 
head.penup()  #turtle module by default draws a line
head.goto(0,0)  #tutle starts at the centr of screen by default
head.direction = "stop"


#  create snake food
food = turtle.Turtle()
food.speed(0) #animation speed of turtle module
food.shape("circle")
food.color("orange") 
food.penup()  #turtle module by default draws a line
food.goto(0,100)  #tutle starts at the centr of screen by default

#growing snake body
segments = []


# Scoring
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score : 0    High Score : 0", align="center", font=("Courier",24,"normal"))


# Function for moving of head
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"



def move():

    y = head.ycor()
    x = head.xcor()


    if head.direction == "up":
        head.sety(y + 20)

    if head.direction == "down":
        head.sety(y - 20)
    
    if head.direction == "left":
        head.setx(x - 20)

    if head.direction == "right":
        head.setx(x + 20)


# keyboard bindings
window.listen()
window.onkeypress(go_up,"Up")
window.onkeypress(go_down,"Down")
window.onkeypress(go_left,"Left")
window.onkeypress(go_right,"Right")

# main game loop
while True:
    window.update()

    # check for border collisions; basically DIE snake Die! XD
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

    
    # restart after collision; REBIRTH of the snake! XD
        for segment in segments:
            segment.goto(1000,1000) #move off-screen

        # clear segments list
        segments.clear()


    if head.distance(food) < 20:
        # move food to random place
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        # Grow the snake body
        new_segment = turtle.Turtle()
        new_segment.speed(0) #animation speed 
        new_segment.shape("square")
        new_segment.color("grey") 
        new_segment.penup()  #turtle module by default draws a line
        segments.append(new_segment) 


    # move segments back-to-up
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    # move segment 0
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)


    move()


    # check for body collisions; DONT EAT SELF!
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # restart after collision; REBIRTH of the snake! XD
            for segment in segments:
                segment.goto(1000,1000) #move off-screen

            # clear segments list
            segments.clear()


    # add delay
    time.sleep(delay)


window.mainloop()