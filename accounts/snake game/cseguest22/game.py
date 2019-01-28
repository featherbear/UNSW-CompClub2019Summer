import turtle
import time
import random

screen = turtle.Screen()
screen.title("This is a game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
difficulty = screen.numinput("Snake Game","Press 1 for Easy, 2 for Medium, 3 for Hard")


head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")

head.penup()
head.goto(0,0)
head.direction = "stop"

speed = 20
def move():
    if head.direction == "stop":
        y = head.ycor()
        head.sety(y + speed)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - speed)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + speed)
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + speed)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - speed)

if difficulty == 1:
    delay = 0.5
elif difficulty == 2:
    delay = 0.1
elif difficulty == 3:
    delay = 0.05



def goUp():
    if head.direction != "down":
        head.direction = "up"

def goDown():
    if head.direction != "up":
        head.direction = "down"

def goLeft():
    if head.direction != "right":
        head.direction = "left"

def goRight():
    if head.direction != "left":
        head.direction = "right"

food = turtle.Turtle()
food.speed(0)
food.shape("turtle")
food.color("red")
food.penup()
food.goto(0,100)

snakeBody = []

def gameStop():
    time.sleep(1)
    head.goto(0,0)
    head.direction = "stop"
    

    for part in snakeBody:
        part.goto(1000,1000)
    
    snakeBody.clear()

while True:
    screen.update()
    time.sleep(delay)
    
    screen.listen()
    screen.onkeypress(goUp, "w")
    screen.onkeypress(goDown, "s")
    screen.onkeypress(goLeft, "a")
    screen.onkeypress(goRight, "d")
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
    
        newBodyPart = turtle.Turtle()
        newBodyPart.speed(0)
        newBodyPart.shape("square")
        newBodyPart.color("green")
        newBodyPart.penup()
        snakeBody.append(newBodyPart)

    for index in range(len(snakeBody) - 1, 0, -1):
        x = snakeBody[index - 1].xcor()
        y = snakeBody[index - 1].ycor()

        snakeBody[index].goto(x,y)
    
    if len(snakeBody) > 0:
        x = head.xcor()
        y = head.ycor()
        snakeBody[0].goto(x, y)

    if head.xcor()>290 or head.xcor() < -290 or head.ycor()>290 or head.ycor()<-290:
        gameStop()

    move()
    for part in snakeBody:
        if part.distance(head) < 20:
            score = 0
            gameStop()

    score = len(snakeBody)
    highscore = 0
    if score >= highscore:
        highscore == score
    else:
        highscore != score


screen.mainloop()
