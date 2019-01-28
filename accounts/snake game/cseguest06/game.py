import turtle
import time
import random

score = 0
highscore = 0

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

snakeBody = []

delay = 0.07
speed = 22

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
	if head.direction != "left":
		head.direction = "right"
	
def gameStop():
	time.sleep(1)
	head.goto(0, 0)
	head.direction = "stop"
	for part in snakeBody:
		part.goto(1000, 1000)
	snakeBody.clear()

while True:
	screen.onkeypress(goUp, "w")
	screen.onkeypress(goDown, "s")
	screen.onkeypress(goLeft, "a")
	screen.onkeypress(goRight, "d")
	screen.update()
	time.sleep(delay)
	screen.listen()	
	if head.distance(food) < 20:
		x = random.randint(-290, 290)
		y = random.randint(-290, 290)
		food.goto(x, y)

		newBodyPart = turtle.Turtle()
		newBodyPart.speed(0)
		newBodyPart.shape("circle")
		newBodyPart.color("white")
		newBodyPart.penup()
		snakeBody.append(newBodyPart)
		score = score + 10
		pen.clear()
		pen.color("white")
		pen.write("Score: " + str(score) + " ---- Highscore: " + str(highscore), align="center", font=("Comic Sans", 15, "normal"))
		
		if(score > highscore):
			highscore = score		

	for index in range(len(snakeBody) - 1, 0, -1):
		x = snakeBody[index - 1].xcor()
		y = snakeBody[index - 1].ycor()
		snakeBody[index].goto(x, y)
	if len(snakeBody) > 0:
		x = head.xcor()
		y = head.ycor()
		
		snakeBody[0].goto(x, y)
	if head.xcor() > 290 or head.xcor() < -290:
		gameStop()
		pen.clear()
		score = 0
	elif head.ycor() > 290 or head.ycor() < -290:
		gameStop()
		pen.clear()
		score = 0

	move()
	
screen.mainloop()


