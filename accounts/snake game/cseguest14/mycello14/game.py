import turtle
import time
import random

colours =  ['blue', 'pink','green','yellow','orange','purple','red','black','white']

screen = turtle.Screen()
screen.title('Turtle game')
screen.bgcolor(colours[random.randint(0,8)])
screen.setup(width=600, height=600)
screen.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color(colours[random.randint(0,8)])
head.penup()
head.goto (0, 0)
head.direction = "stop"

head1 = turtle.Turtle()
head1.speed(0)
head1.shape("square")
head1.color(colours[random.randint(0,8)])
head1.penup()
head1.goto (0, 0)
head1.direction = "stop

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
	if head1.direction == "up":
		y = head1.ycor()
		head1.sety(y + speed)
	elif head1.direction == "down":
		y = head1.ycor()
		head1.sety(y - speed)
	elif head1.direction == "left":
		x = head.xcor()
		head.setx(x - speed)
	elif head1.direction == "right":
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

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color(colours[random.randint(0,8)])
food.penup()
food.goto(0 ,100)
snakeBody = []

food2 = turtle.Turtle()
food2.speed(0)
food2.shape("circle")
food2.color(colours[random.randint(0,8)])
food2.penup()
food2.goto(0 ,100)
snakeBody = []


food1 = turtle.Turtle()
food1.speed(0)
food1.shape("circle")
food1.color(colours[random.randint(0,8)])
food1.penup()
food1.goto(0 ,100)
snakeBody = []
while True:
	screen.update()
	time.sleep(delay)
	screen.listen()
	screen.onkeypress(goUp, 'w')
	screen.onkeypress(goDown, 's')
	screen.onkeypress(goLeft, 'a')
	screen.onkeypress(goRight, 'd')
	
	if head.distance(food) < 20:
		x = random.randint(-290,290)
		y = random.randint(-290,290)
		food.goto(x, y)
		newBodyPart = turtle.Turtle()
		newBodyPart.speed(0)
		newBodyPart.shape("square")
		newBodyPart.color(colours[random.randint(0,8)])
		newBodyPart.penup()
		snakeBody.append(newBodyPart)


	if head.distance(food1) < 20:
		x = random.randint(-290,290)
		y = random.randint(-290,290)
		food1.goto(x, y)
		newBodyPart = turtle.Turtle()
		newBodyPart.speed(0)
		newBodyPart.shape("square")
		newBodyPart.color(colours[random.randint(0,8)])
		newBodyPart.penup()
		snakeBody.append(newBodyPart)


	if head.distance(food2) < 20:
		x = random.randint(-290,290)
		y = random.randint(-290,290)
		food2.goto(x, y)
		newBodyPart = turtle.Turtle()
		newBodyPart.speed(0)
		newBodyPart.shape("square")
		newBodyPart.color(colours[random.randint(0,8)])
		newBodyPart.penup()
		snakeBody.append(newBodyPart)
		

	for index in range(len(snakeBody) - 1, 0, -1):
		x = snakeBody[index - 1].xcor()
		y = snakeBody[index - 1].ycor()

		snakeBody[index].goto(x, y)


	if len(snakeBody) > 0:
		x = head.xcor()
		y = head.ycor()

		snakeBody[0].goto(x, y)
	

	if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
		gameStop()
	move()
	for part in snakeBody:
		if part.distance(head) < 1:
			score = 0 
			gameStop()
 
	

screen.mainloop()	
















