import turtle
import time
import random

screen = turtle.Screen()
screen.title("Snake 2")
screen.bgcolor("black")
screen.setup(width=600, height = 600)
screen.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")

head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0 ,100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("purple")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

score = 0

highScore = 0

pen.clear()
pen.write("Score: " + str(score) + "      High Score: " + str(highScore), align = "center", font = ("Courier", 24, "normal"))

delay = 0.1

speed = 20
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + speed)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - speed)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - speed)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + speed)

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
    if head.direction !="left":
        head.direction = "right"

screen.listen()
screen.onkeypress(goUp, 'w')
screen.onkeypress(goDown, 's')
screen.onkeypress(goLeft, 'a')
screen.onkeypress(goRight, 'd')
screen.onkeypress(goUp, 'Up')
screen.onkeypress(goDown, 'Down')
screen.onkeypress(goLeft, 'Left')
screen.onkeypress(goRight, 'Right')
snakeBody = []

colors = ["red", "orange", "yellow", "green", "blue", "purple"]



def gameStop():
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"
    score = 0
    pen.clear()
    pen.write("Score: " + str(score) + "      High Score: " + str(highScore), align = "center", font = ("Courier", 24, "normal"))
    for part in snakeBody:
        part.goto(1000, 1000)

    snakeBody.clear()

while True:
    screen.update()
    time.sleep(delay)
    
    i = random.randint(0,5)

    if head.distance(food) <20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 280)
        food.goto(x, y)
        score = score + 1

        if score > highScore: 
            highScore = highScore + 1
        pen.clear()
        pen.write("Score: " + str(score) + "      High Score: " + str(highScore), align = "center", font = ("Courier", 24, "normal"))
        newBodyPart = turtle.Turtle()
        newBodyPart.speed(0)
        newBodyPart.shape("square")
        newBodyPart.color(colors[i])
        newBodyPart.penup()
        snakeBody.append(newBodyPart)
    
    for index in range(len(snakeBody)-1, 0, -1):
        x = snakeBody[index - 1].xcor()
        y = snakeBody[index - 1].ycor()
        snakeBody[index].goto(x, y)
    
    if len(snakeBody) >0:
        x = head.xcor()
        y = head.ycor()
        snakeBody[0].goto(x, y)

    if head.xcor() >290 or head.xcor() < -290:
        gameStop()
        score = 0

    if head.ycor() >290 or head.ycor() < -290:
        gameStop()
        score = 0
    move()

    for part in snakeBody:
        if part.distance(head) < 1:
            score = 0
            gameStop()


screen.mainloop()
