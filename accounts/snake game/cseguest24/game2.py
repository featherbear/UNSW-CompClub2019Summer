import turtle
import time
import random

score = 0
highscore = 0

screen = turtle.Screen()
screen.title('Snake')
screen.bgcolor('white')
screen.setup(width = 600, height = 600)
screen.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("blue")

head.penup()
head.goto(0,0)
head.direction = "stop"
speed = 10


pen = turtle.Turtle()
pen.goto(0, 260)



def move():
	if head.direction == 'up':
		y=head.ycor()
		head.sety(y+speed)
	if head.direction == 'down':
		y=head.ycor()
		head.sety(y-speed)
	if head.direction == 'right':
		x=head.xcor()
		head.setx(x+speed)
	if head.direction == 'left':
		x=head.xcor()
		head.setx(x-speed)

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


def gameStop():
	score= 0
	time.sleep(1)
	head.goto(0, 0)
	head.direction = 'stop'
	for part in snakeBody:
		part.goto(1000, 1000)
	pen.clear()
	pen.write("Score " + str(score) + " Highscore " + str(highscore), align = "center", font = ("courier", 24, "normal"))
	snakeBody.clear()


pen.write("Score " + str(score) + " Highscore " + str(highscore), align = "center", font = ("courier", 24, "normal"))

screen.listen()
screen.onkeypress (goUp, 'w')
screen.onkeypress(goDown, 's')
screen.onkeypress(goLeft, 'a')
screen.onkeypress(goRight, 'd')
delay = 0.1

food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('orange')
food.penup()
food.goto(0, 100)



snakeBody = []

colours = ['red', 'orange', 'yellow', 'green', 'lightgreen', 'blue', 'lightblue', 'purple', 'pink',]
number = 0

while True: 
	screen.update()
	time.sleep(delay)
	move()
	counter = 0
	for x in range (0, (len(snakeBody)-1)):
		snakeBody[x].color(colours[(x + 1)%9])
		x = x + 1
	x = 0
	

	if head.distance(food) < 20:
		x = random.randint(-290, 290)
		y = random.randint(-290, 290)
		food.goto(x, y)


		newBodyPart = turtle.Turtle()
		newBodyPart.speed(0)
		newBodyPart.shape('circle')
		newBodyPart.color(colours[number])
		number = (number + 1)%9
		newBodyPart.penup()
		snakeBody.append(newBodyPart)
		
		
		score = score + 1
		if score > highscore:
			highscore = score

		pen.clear()
		pen.write("Score " + str(score) + " Highscore " + str(highscore), align = "center", font = ("courier", 24, "normal"))

	for index in range(len(snakeBody) -1,0,-1):
		x = snakeBody[index-1].xcor()
		y = snakeBody[index-1].ycor()
		snakeBody[index].goto(x,y)

	if len(snakeBody)>0:
		x = head.xcor()
		y = head.ycor()

		snakeBody[0].goto(x,y)



	
	if head.xcor()>290 or head.xcor()<-290:
		gameStop()
		score= 0
	if head.ycor()>290 or head.ycor()<-290:
		gameStop()
		score = 0
	for part in snakeBody[1:]:
		if part.distance(head)<1:
			score = 0
			gameStop()


			
	







screen.mainloop()


