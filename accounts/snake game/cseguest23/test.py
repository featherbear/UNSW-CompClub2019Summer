import turtle
import time
import random

screen = turtle.Screen()
screen.title("Homemade Snake Game CompClub 2019")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")

head.penup()
head.goto(0,0)
head.direction = "stop"

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
    if head.direction != "up":
        head.direction = "down"
def goLeft():
    if head.direction != "right":
        head.direction = "left"
def goRight():
    if head.direction != "left":
        head.direction = "right"

screen.listen()
screen.onkeypress(goUp, 'w')
screen.onkeypress(goDown, 's')
screen.onkeypress(goLeft, 'a')
screen.onkeypress(goRight, 'd')
'''
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0,100)

snakeBody = []


for index in range (len(snakeBody) -1, 0, -1):
	x = snakeBody[index - 1].xcor()
	y = snakeBody[index - 1].ycor()

	snakeBody[index].goto(x, y)

if len(snakeBody)  > 0:
	x = head.xcor()
	y = head.ycor()

	snakeBody[0].goto(x, y)

'''
delay = 0.1
while True:
	screen.update()
	time.sleep(delay)
	move()
'''
	if head.distance(food) < 20:
		x = random.randint(-290, 290)
		y = random.randint(-290, 290)
		food.goto(x, y)

		newBodyPart = turtle.Turtle()
		newBodyPart.speed(0)
		newBodyPart.shape("square")
		newBodyPart.color("green")
		newBodyPart.penup()
		snakeBody.append(newBodyPart)
'''
screen.mainloop()
