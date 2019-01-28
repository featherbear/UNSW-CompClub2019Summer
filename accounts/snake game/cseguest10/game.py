import turtle
import time
import random
snakeBody = []
colors = ['dark violet', 'hot pink', 'dodger blue', 'slate blue', 'deep sky blue', 'orchid']
randomcolour = random.choice(colors)

screen = turtle.Screen()
screen.title("Snake")
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape('circle')
head.color('blue')
head.penup()
head.goto(0, 0)
head.direction ='stop'

food = turtle.Turtle()
food.speed(0) 
food.shape("circle") 
food.color("red")
food.penup()
food.goto(0 ,100)

score = 0
highscore = 0
pen = turtle.Turtle()
pen.speed(0)
pen.shape('circle')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Score:' + str(score) + "---- High Score: " + str(highscore), align="center", font = ("Courier",24, "normal"))
delay = 0.1
speed = 20
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
	elif head. direction == 'right':
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


screen.listen()
screen.onkeypress(goUp, 'w')
screen.onkeypress(goDown, 's')
screen.onkeypress(goLeft, 'a')
screen.onkeypress(goRight, 'd')

while True:

	if head.distance(food) < 20: #If im close enough ill eat the food
		x = random.randint(-290, 290)
		y = random.randint(-290, 290)
		food.goto(x, y)
		#everytime I eat I growwww
		newBodyPart = turtle.Turtle()
		newBodyPart.speed(0)
		newBodyPart.shape("circle")
		randomcolour = random.choice(colors)
		newBodyPart.color(randomcolour)
		newBodyPart.penup()
		snakeBody.append(newBodyPart)
		score = score + 1
		if score > highscore: 
			highscore = score
		pen.clear()
		pen.write('Score:' + str(score) + "---- High Score: " + str(highscore), align="center", font = ("Courier",24, "normal"))
	for index in range(len(snakeBody) - 1, 0, -1):  #The body, except for the first index, will get the coordinates of the prev index                                               
		x = snakeBody[index - 1].xcor()        
		y = snakeBody[index - 1].ycor()
		snakeBody[index].goto(x, y)
	if len(snakeBody) > 0: #First body goes to head position
		x = head.xcor()
		y = head.ycor()
		snakeBody[0].goto(x, y)
	move()
	if head.xcor() > 290 or head.ycor() > 290  or head.xcor() < -290 or head.ycor() < -290:
		gameStop()
		score = 0

	for part in snakeBody:
		if part.distance(head) < 1:
			score = 0
			gameStop()
		#moves head
	screen.update()
	time.sleep(delay)


screen.mainloop()
