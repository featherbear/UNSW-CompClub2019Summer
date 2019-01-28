import turtle
import time
import random
score2 = 0
hscore = 0
score3 = 0
hscore2 = 0
def write():
	turtle.goto(0,260)
	turtle.clear()
	turtle.color("white")
	turtle.write("Score" + str(score2) + "----Highscore" + str(hscore), align = "center", font=	("Courier",24,"normal"))
	turtle.hideturtle()
def write2():
	turtle.goto(0,225)
	turtle.clear()
	turtle.color("white")
	turtle.write("Score" + str(score3) + "----Highscore" + str(hscore2), align = "center", font=	("Courier",24,"normal"))
	turtle.hideturtle()


screen = turtle.Screen()
screen.title('Turtle game')
screen.bgcolor('green')
screen.setup(width=600, height=600)
screen.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("purple")
head.penup()
head.goto (0, 0)
head.direction = "stop"

head2 = turtle.Turtle()
head2.speed(0)
head2.shape("square")
head2.color("purple")
head2.penup()
head2.goto (0, 0)
head2.direction = "stop"

delay = 0.075
speed = 21.5
write()

def move2():
	if head2.direction == "up":
		y = head2.ycor()
		head2.sety(y + speed)
	elif head2.direction == "down":
		y = head2.ycor()
		head2.sety(y - speed)
	elif head2.direction == "left":
		x = head2.xcor()
		head2.setx(x - speed)
	elif head2.direction == "right":
		x = head2.xcor()
		head2.setx(x + speed)

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

def K1():
	if head2.direction != "down":
		head2.direction = "up"

def K2():
	if head2.direction != "up":
		head2.direction = "down"
def K3():
	if head2.direction != "right":
		head2.direction = "left"
def K4():
	if head2.direction != "left":
		head2.direction = "right"
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0 ,100)
snakeBody = []
snakeBody2 = []
colours = ['white', 'yellow', 'brown','red', 'orange', 'black', 'blue']

def gameStop():
	global score2
	time.sleep(1)
	head.goto(0, 0)
	head.direction = "stop"
	for part in snakeBody:
		part.goto(1000,1000)
	score2 = 0
	write()
	snakeBody.clear()
	

		
while True:
	screen.update()
	time.sleep(delay)
	screen.listen()
	screen.onkeypress(goUp, 'w')
	screen.onkeypress(goDown, 's')
	screen.onkeypress(goLeft, 'a')
	screen.onkeypress(goRight, 'd')
	screen.onkeypress(K1, 'Up')
	screen.onkeypress(K2, 'Down')
	screen.onkeypress(K3, 'Left')
	screen.onkeypress(K4, 'Right')
	if head.distance(food) < 20:
		x = random.randint(-280,250)
		y = random.randint(-280,250)
		food.goto(x, y)
		newBodypart = turtle.Turtle()
		newBodypart.speed(0)
		newBodypart.shape("square")
		newBodypart.color(colours[random.randint(0,6)])
		newBodypart.penup()
		snakeBody.append(newBodypart)
	if head2.distance(food) < 20:
		x = random.randint(-200,200)
		y = random.randint(-200,200)
		food.goto(x, y)
		newBodypart2 = turtle.Turtle()
		newBodypart2.speed(0)
		newBodypart2.shape("square")
		newBodypart2.color(colours[random.randint(0,6)])
		newBodypart2.penup()
		snakeBody2.append(newBodypart2)
		score3 += 1
		write2()
	if score2 > hscore:
		hscore= score2
		write()
	if score3 > hscore2:
		hscore2 = score3

	

	for index in range (len(snakeBody) - 1,0, -1):
		x = snakeBody[index - 1].xcor()
		y = snakeBody[index - 1].ycor()
		
		snakeBody[index].goto(x, y)
	if len(snakeBody) > 0:
		x = head.xcor()
		y = head.ycor()
		snakeBody[0].goto(x, y)
	if head.xcor() > 200 or head.xcor() < -200 or head.ycor() > 200 or head.ycor() < -200:
		gameStop()

	for index in range (len(snakeBody2) - 1,0, -1):
		x = snakeBody2[index - 1].xcor()
		y = snakeBody2[index - 1].ycor()
		
		snakeBody2[index].goto(x, y)
	if len(snakeBody2) > 0:
		x = head2.xcor()
		y = head2.ycor()
		snakeBody2[0].goto(x, y)
	if head2.xcor() > 200 or head2.xcor() < -200 or head2.ycor() > 200 or head2.ycor() < -200:
		gameStop()

	move()
	move2()

	for part in snakeBody:
		if part.distance(head) < 1:
			score = 0
			gameStop()

screen.mainloop()

