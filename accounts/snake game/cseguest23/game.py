import turtle
import time
import random

score=0
highScore=0
colour = ['red', 'green', 'blue', 'purple', 'black', 'pink', 'brown', 'orange', 'yellow']

screen = turtle.Screen()
screen.title('Snake')
screen.bgcolor('green')
screen.setup(width = 600, height = 600)
screen.tracer(0)

head=turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('red')

head.penup()
head.goto(0, 0)
head.direction = 'stop'

food = turtle.Turtle()
food.speed(0)
food.shape('turtle')
food.color('yellow')
food.penup()
food.goto(0 ,100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

delay = 0.1
speed = 100

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + speed)
    elif head.direction == 'down':
        y = head.ycor()
        head.sety(y - speed)
    elif head.direction == 'left':
        x = head.xcor()
        head.setx(x - speed)
    elif head.direction == 'right':
        x = head.xcor()
        head.setx(x + speed)

def goUp():
    if head.direction != 'down':
        head.direction = 'up'

def goDown():
    if head.direction != 'up':
        head.direction = 'down'

def goLeft():
    if head.direction != 'right':
        head.direction = 'left'

def goRight():
    if head.direction != 'left':
        head.direction = 'right'

screen.listen()
screen.onkeypress(goUp, 'w')
screen.onkeypress(goDown, 's')
screen.onkeypress(goLeft, 'a')
screen.onkeypress(goRight, 'd')

def gameStop():
    time.sleep(1)
    head.goto(0, 0)
    head.direction = 'stop'
    score = 0
    for part in snakeBody:
        part.goto(1000, 1000)

    snakeBody.clear()

snakeBody = []
while True:
    screen.update()
    time.sleep(delay)
    i =random.randint(0, 9)
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        newBodyPart = turtle.Turtle()
        newBodyPart.speed(0)
        newBodyPart.shape('square')
        newBodyPart.color(colour[i])
        newBodyPart.penup()
        snakeBody.append(newBodyPart)
        score = score + 1
        if score > highScore:
            highScore=highScore+1
    for index in range(len(snakeBody) -1, 0, -1):
        x = snakeBody[index - 1].xcor()
        y = snakeBody[index - 1].ycor()

        snakeBody[index].goto(x, y)
    if len(snakeBody) > 0:
        x = head.xcor()
        y = head.ycor()

        snakeBody[0].goto(x, y)
    if head.xcor() > 290 or head.xcor() < -290:
        gameStop()
    if head.ycor() > 290 or head.ycor() < -290:
        gameStop()
    move()
    for part in snakeBody:
        if part.distance(head) <1:
            score = 0
            gameStop()
    pen.clear()
    pen.write('Score: ' + str(score) + '---- High Score:' + str(highScore), align='center', font = ("Courier", 24,'normal' ))

screen.mainloop()
