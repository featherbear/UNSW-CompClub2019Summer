import turtle
import time
from random import randint

print("Welcome to the Snake game!")
print("The rules are simple: ")
print("1. Don't touch the sides of the screen ")
print("2. Don't touch the end of your tail ")
print("3. Collect as many coins as possible ")
colour = input("Choose your colour: red or blue? ")

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("triangle")
head.color(colour)

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0, 100)

food2 = turtle.Turtle()
food2.speed(0)
food2.shape("circle")
food2.color("yellow")
food2.penup()
food2.goto(0, 100)

head.penup()
head.goto(0, 0)
head.direction = "stop"

score = 0

highScore = 0

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color(colour)
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: " + str(score) + "---- High Score: " + str(highScore), align="center", font=("Courier", 24, "normal"))

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
		head.left(90)

def goDown():
    if head.direction !="up":
        head.direction = "down"
        head.right(90)

def goLeft():
    if head.direction !="right":
        head.direction = "left"
        head.right(60)

def goRight():
    if head.direction !="left":
        head.direction = "right"
        head.left(60)
        
def gameStop():
	time.sleep(1)
	head.goto(0, 0)
	head.direction = "stop"
	score = 0
	pen.clear()
	pen.write("Score: " + str(score) + "---- High Score: " + str(highScore), align="center", font=("Courier", 24, "normal"))
	
	for part in snakeBody:
		part.goto(1000, 1000)
	
	snakeBody.clear()
		
screen.listen()
screen.onkeypress(goUp, 'w')
screen.onkeypress(goDown, 's')
screen.onkeypress(goLeft, 'a')
screen.onkeypress(goRight, 'd')

snakeBody = []

while True:
	screen.update()
	time.sleep(delay)
	if head.distance(food) < 20:
		x = randint(-290, 290)
		y = randint(-290, 290)
		food.goto(x,y)
		newBodyPart = turtle.Turtle()
		newBodyPart.speed(0)
		newBodyPart.shape("square")
		newBodyPart.color(colour)
		newBodyPart.penup()
		snakeBody.append(newBodyPart)
		score = score + 1
		if score > highScore:
			highScore = score
		pen.clear()
		pen.write("Score: " + str(score) + "---- High Score: " + str(highScore), align="center", font=("Courier", 24, "normal"))
	if head.distance(food2) < 20:
		x = randint(-290, 290)
		y = randint(-290, 290)
		food2.goto(x,y)
		newBodyPart = turtle.Turtle()
		newBodyPart.speed(0)
		newBodyPart.shape("square")
		newBodyPart.color(colour)
		newBodyPart.penup()
		snakeBody.append(newBodyPart)
		score = score + 1
		if score > highScore:
			highScore = score
		pen.clear()
		pen.write("Score: " + str(score) + "---- High Score: " + str(highScore), align="center", font=("Courier", 24, "normal"))
	for index in range(len(snakeBody) - 1, 0, -1):
		print(index)
		x = snakeBody[index - 1].xcor()
		y = snakeBody[index - 1].ycor()
		snakeBody[index].goto(x, y)
	if len(snakeBody) > 0:
		x = head.xcor()
		y = head.ycor()
		snakeBody[0].goto(x, y)
	move()
	if head.xcor() > 290 or head.xcor() < -290:
		score = 0
		gameStop()
	if head.ycor() > 290 or head.ycor() < -290:
		score = 0
		gameStop()
	for part in snakeBody:
		if part.distance(head) < 1:
			score = 0
			gameStop()

screen.mainloop()



