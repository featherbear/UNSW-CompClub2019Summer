import turtle
import time
import random
score = 0
score2 = 0
highscore2 = 0
highscore = 0
speed = 20
def randommove(a):
	x1 = a.xcor()
	y1 = a.ycor()
	a.goto(random.randint(-20,20)+x1, random.randint(-20,20)+y1)
	
def move(head):
	if head.direction == "up":
		y = head.ycor()
		head.sety(y + speed)
	elif head.direction == "down":
		y = head.ycor()
		head.sety(y - speed)
	elif head.direction == "left":
		x = head.xcor()
		head.setx(x-speed)
	elif head.direction == "right":
		x = head.xcor()
		head.setx(x+speed)
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
def Up():
	if head2.direction != "down":
		head2.direction = "up"
def Down():
	if head2.direction != "up":
		head2.direction = "down"
def Left():
	if head2.direction != "right":
		head2.direction = "left"
def Right():
	if head2.direction != "left":
		head2.direction = "right"


def write():
	turtle.goto(0,460)
	turtle.clear()
	turtle.color('blue')
	turtle.write("Score: " + str(score)+ " ---- High Score: " + str(highscore), align="center", font=("Courier", 24, "normal "))
	turtle.penup()
	turtle.goto(0,360)
	turtle.color('blue')
	turtle.pendown()
	turtle.write("Score2: " + str(score2)+ " ---- High Score2: " + str(highscore2), align="center", font=("Courier", 24, "normal "))
	turtle.hideturtle()
def gameStop():
	global score
	time.sleep(1)
	head.goto(-300, 0)
	head.direction = "stop"
	score = 0
	write()
	for part in snakeBody:
		part.goto(2000, 2000)
	snakeBody.clear()
def gameStop2():
	global score2
	time.sleep(1)
	head2.goto(300, 0)
	head2.direction = "stop"
	score2 = 0
	write()
	for part in snakeBody2:
		part.goto(2000, 2000)
	snakeBody2.clear()
screen = turtle.Screen()
screen.title("SNAKE!!!")
screen.bgcolor("black")
screen.setup(width=1000, height=1000)
screen.tracer(0)
write()
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue") 
head.penup()
head.goto(-300,0)
head.direction = "stop"
head2 = turtle.Turtle()
head2.speed(0)
head2.shape("square")
head2.color("grey") 
head2.penup()
head2.goto(300,0)
head2.direction = "stop"
delay = 0.1
food = turtle.Turtle()
food.speed(0) 
food.shape("circle") 
food.color("yellow")
food.penup()
food.goto(random.randint(-480, 480) ,random.randint(-480, 480))
food2 = turtle.Turtle()
food2.speed(0) 
food2.shape("circle") 
food2.color("yellow")
food2.penup()
food2.goto(random.randint(-480, 480) ,random.randint(-480, 480))
snakeBody = []
snakeBody2 = []
colours = ["white", "purple", 'green', 'brown', 'pink', 'yellow', 'red', 'orange']



while True:
	screen.update()
	time.sleep(delay)
	screen.listen()
	screen.onkeypress(goUp, 'w')
	screen.onkeypress(goDown, 's')
	screen.onkeypress(goLeft, 'a')
	screen.onkeypress(goRight, 'd')
	screen.onkeypress(Up, 'Up')
	screen.onkeypress(Down, 'Down')
	screen.onkeypress(Left, 'Left')
	screen.onkeypress(Right, 'Right')
	if head.distance(food) < 20:
		score += 1
		write()
		x = random.randint(-480, 480)
		y = random.randint(-480, 480)
		food.goto(x, y)
		newBodyPart = turtle.Turtle()
		newBodyPart.speed(0)
		newBodyPart.shape("square")
		newBodyPart.color(colours[random.randint(0,7)])
		newBodyPart.penup()
		snakeBody.append(newBodyPart)
	if head.distance(food2) < 20:
		score += 1
		write()
		x = random.randint(-480, 480)
		y = random.randint(-480, 480)
		food2.goto(x, y)
		newBodyPart = turtle.Turtle()
		newBodyPart.speed(0)
		newBodyPart.shape("square")
		newBodyPart.color(colours[random.randint(0,7)])
		newBodyPart.penup()
		snakeBody.append(newBodyPart)
	for index in range(len(snakeBody) - 1, 0, -1):
		x = snakeBody[index - 1].xcor()
		y = snakeBody[index - 1].ycor()
		snakeBody[index].goto(x, y)
	if len(snakeBody)>0:
		x = head.xcor()
		y = head.ycor()
		snakeBody[0].goto(x, y)
	if head2.distance(food) < 20:
		score2 += 1
		write()
		x = random.randint(-480, 480)
		y = random.randint(-480, 480)
		food.goto(x, y)
		newBodyPart2 = turtle.Turtle()
		newBodyPart2.speed(0)
		newBodyPart2.shape("square")
		newBodyPart2.color(colours[random.randint(0,7)])
		newBodyPart2.penup()
		snakeBody2.append(newBodyPart2)
	if head2.distance(food2) < 20:
		score2 += 1
		write()
		x = random.randint(-480, 480)
		y = random.randint(-480, 480)
		food2.goto(x, y)
		newBodyPart2 = turtle.Turtle()
		newBodyPart2.speed(0)
		newBodyPart2.shape("square")
		newBodyPart2.color(colours[random.randint(0,7)])
		newBodyPart2.penup()
		snakeBody2.append(newBodyPart2)
	for index in range(len(snakeBody2) - 1, 0, -1):
		x = snakeBody2[index - 1].xcor()
		y = snakeBody2[index - 1].ycor()
		snakeBody2[index].goto(x, y)
	if len(snakeBody2)>0:
		x = head2.xcor()
		y = head2.ycor()
		snakeBody2[0].goto(x, y)
	if head.xcor() > 500 or head.xcor() < -500 or head.ycor() > 500 or head.ycor() < -500:
		score = 0
		gameStop()
	if head2.xcor() > 500 or head2.xcor() < -500 or head2.ycor() > 500 or head2.ycor() < -500:
		score2 = 0
		gameStop2()
	if score > highscore:
		highscore = score
		write()
	if score2 > highscore2:
		highscore2 = score2
		write()
	if head2.distance(head)<1:
		score = 0
		score2 = 0
		gameStop2()
		gameStop()
	move(head)
	move(head2)
	for part in snakeBody:
		if part.distance(head) < 1:
			score = 0
			gameStop()
	for part in snakeBody2:
		if part.distance(head2) < 1:
			score = 0
			gameStop2()

screen.mainloop()



