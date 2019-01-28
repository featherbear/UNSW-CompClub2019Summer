import turtle
import time
import random

snakeBody = []

score = 0 
highscore = 0

food_color = ["blue", "red," "pink,"]

pen = turtle.Turtle()
pen.color ("White")
pen.sety

screen = turtle.Screen()
screen.title("A")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

head = turtle.Turtle() 
head.speed(0)
head.shape("square")
head.color("green")

head.penup()
head.goto(0 ,0)
head.direction = "stop"



def move():
	if head.direction == "up":
		y = head.ycor()
		head.sety(y + speed)
	elif head.direction == "down":
		y = head.ycor ()
		head.sety(y - speed)
	elif head.direction == "right":
		x = head.xcor()
		head.setx (x + speed)
	elif head.direction == "left":
		x = head.xcor()
		head.setx (x - speed)

def goDown():
	if head.direction != "up":
		head.direction = "down"
def goUp():
	if head.direction != "down":
		head.direction = "up"
def goRight():
	if head.direction != "left":
		head.direction = "right"
def goLeft():
	if head.direction != "right":
		head.direction = "left"

screen.listen()
screen.onkeypress(goUp, 'w')
screen.onkeypress(goDown, 's')
screen.onkeypress(goLeft, 'a')
screen.onkeypress(goRight, 'd')

	
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0,100)





def gameStop():
	global score
	global speed
	score = 0
	time.sleep(1)
	head.goto(0,0)
	speed = 20
	head.direction = "stop"
	
	
	for part in snakeBody:
		part.goto(1000, 1000,)
	
	snakeBody.clear()
SBC = ["white", "red", "blue", "green", "yellow", "pink", "purple"]



speed = 20
delay = 0.1
while True:

	pen.clear()
	pen.write("score:" + str(score)+ "---highscore:" +str(highscore), align="center",font=("Courier", 24 , "normal"))

	screen.update()
	time.sleep(delay)
	if head.distance(food) < speed:
		x = random.randint(-290,290)
		y = random.randint(-290,290)
		food.goto(x,y)
		score = score + 1
		speed = speed * 1

		newBodyPart = turtle.Turtle()
		newBodyPart.speed(0)
		newBodyPart.shape("square")
		newBodyPart.color(random.choice(SBC))
		newBodyPart.penup()
		snakeBody.append(newBodyPart)
		
	
	if highscore < score:
                highscore = score
		
	for index in range(len(snakeBody) - 1, 0, -1):
		x = snakeBody [index - 1].xcor()
		y = snakeBody [index - 1].ycor()

		snakeBody[index].goto(x, y)
	if len(snakeBody) > 0:
		x = head.xcor()
		y = head.ycor()

		snakeBody[0].goto(x, y)
	if head.xcor() > 290 or head.xcor() < -290:
		score = 0
		gameStop()
	if head.ycor() > 290 or head.ycor() < -290:
		score = 0
		gameStop()
		
	for part in snakeBody[1: ]:
		if part.distance(head) < 1:
			score = 0
			gameStop()

	
		
		



	move()


screen.mainloop()



