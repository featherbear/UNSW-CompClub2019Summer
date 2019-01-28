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

speed = 2
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

def speed_1x():
	speed = 2
	#print("2")

def speed_2x():
	speed = 4
	#print("4")

screen.listen()
screen.onkeypress(goUp, 'w')
screen.onkeypress(goDown, 's')
screen.onkeypress(goLeft, 'a')
screen.onkeypress(goRight, 'd')
screen.onkeypress(speed_1x, '1')
screen.onkeypress(speed_2x, '2')

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0,100)

snakeBody = []

highScore = 0
score = 0
new_bodypart_x10_counter = 0

def gameStop():
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"
    pen.clear()
    pen.write("Score: " + str(score)+ " ---- High Score: " + str(highScore), align="center", font=("Courier", 24, "normal "))
    for part in snakeBody:
	     part.goto(1000, 1000)

    snakeBody.clear()

pen=turtle.Turtle()
pen.color("white")
pen.write("Score: " + str(score)+ " ---- High Score: " + str(highScore), align="center", font=("Courier", 24, "normal ")) 


delay = 0.01
while True:
	print(speed)
	screen.update()
	time.sleep(delay)


	if head.distance(food) < 20:
		x = random.randint(-290, 290)
		y = random.randint(-290, 290)
		food.goto(x, y)

		while new_bodypart_x10_counter < 10:
			newBodyPart = turtle.Turtle()
			newBodyPart.speed(0)
			newBodyPart.shape("square")
			newBodyPart.color("green")
			newBodyPart.penup()
			snakeBody.append(newBodyPart)
			print(new_bodypart_x10_counter)
			new_bodypart_x10_counter = new_bodypart_x10_counter + 1
			
		score = score + 1

		new_bodypart_x10_counter = 0

		if score > highScore:
			highScore=score
		pen.clear()
		pen.write("Score: " + str(score)+ " ---- High Score: " + str(highScore), align="center", font=("Courier", 24, "normal ")) 
		

		pen.clear()
		pen.write("Score: " + str(score)+ " ---- High Score: " + str(highScore), align="center", font=("Courier", 24, "normal ")) 


	for index in range (len(snakeBody) -1, 0, -1):
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
	
	for part in snakeBody[1: ]:
		if part.distance(head) < 1:
			score = 0
			gameStop()




screen.mainloop()


