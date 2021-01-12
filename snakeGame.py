import turtle
import time

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


# Function for moving of head
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
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

#main game loop
while True:
    window.update()

    move()

    # add delay
    time.sleep(delay)


window.mainloop()