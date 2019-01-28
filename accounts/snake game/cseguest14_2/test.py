import turtle
import time
from random import randint

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0, 100)

head.penup()
head.goto(0, 0)
head.direction = "stop"

randlist = []
randcounter = 0

delay = 0.1

speed = 20

def move():
    if head.direction == "up":
	    y = head.ycor()
	    head.sety(y + speed)
    if head.direction == "down":
	    y = head.ycor()
	    head.sety(y - speed)
    if head.direction == "right":
	    x = head.xcor()
	    head.setx(x + speed)
    if head.direction == "left":
	    x = head.xcor()
	    head.setx(x - speed)

def goUp():
	if head.direction != "down":
		head.direction = "up"

def goDown():
    if head.direction !="up":
        head.direction = "down"

def goLeft():
    if head.direction !="right":
        head.direction = "left"

def goRight():
    if head.direction !="left":
        head.direction = "right"
        
def gameStop():
	time.sleep(1)
	head.goto(0, 0)
	head.direction = "stop"
	
	for part in snakeBody:
		part.goto(1000, 1000)
	
	snakeBody.clear()
		
screen.listen()
screen.onkeypress(goUp, 'w')
screen.onkeypress(goDown, 's')
screen.onkeypress(goLeft, 'a')
screen.onkeypress(goRight, 'd')

snakeBody = []

newBodyPart = turtle.Turtle()
newBodyPart.speed(0)
newBodyPart.shape("square")
newBodyPart.color("white")
newBodyPart.penup()
snakeBody.append(newBodyPart)

while True:
	screen.update()
	time.sleep(delay)
	if head.distance(food) < 20:
		x = randint(-290, 290)
		y = randint(-290, 290)
		food.goto(x,y)
	for index in range(len(snakeBody) - 1, 0, -1):
		x = snakeBody[index - 1].xcor()
		snakeBody[index].goto(x, y)
	if len(snakeBody) > 0:
		x = head.xcor()
		y = head.ycor()
		snakeBody[0].goto(x, y)
	if head.xcor() > 290 or head.xcor() < -290:
		gameStop()
	if head.ycor() > 290 or head.ycor() < -290:
		gameStop()
	for part in snakeBody:
		if part.distance(head) < 1:
			score = 0
			gameStop()
			newBodyPart = turtle.Turtle()
			newBodyPart.speed(0)
			newBodyPart.shape("square")
			newBodyPart.color("white")
			newBodyPart.penup()
			snakeBody.append(newBodyPart)
	move()

screen.mainloop()



