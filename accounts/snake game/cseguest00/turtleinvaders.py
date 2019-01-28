import turtle
import os
import math
import random

wn = turtle.Screen()
wn.bgcolor("#2c6d46")
wn.title("Turtle invaders")
wn.bgpic ("space_invaders_background.gif")

turtle.register_shape("invader.gif")
turtle.register_shape("elon2.gif")
turtle.register_shape("laser2.gif")

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("red")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown
border_pen.pensize(3)
for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()

score=0

score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Times New Roman", 14, "normal"))
score_pen.hideturtle()

player = turtle.Turtle()
player.color("blue")
player.shape("elon2.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

number_enemies = 5
number_enemies2 = 5
enemies = []

for i in range(number_enemies):
	enemies.append(turtle.Turtle())

for enemy in enemies:
	enemy.color("orange")
	enemy.shape("invader.gif")
	enemy.penup()
	enemy.speed(0)
	x = random.randint(-200, 200)
	y = random.randint(100, 250)
	enemy.setposition(x, y)

enemyspeed = 4

bullet = turtle.Turtle()
bullet.color("red")
bullet.shape("laser2.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.8, 0.8)
bullet.hideturtle()

bulletspeed = 30

#define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"

def move_left():
	x = player.xcor()
	x -= playerspeed
	if x < -280:
		x = -280
	player.setx(x)

def move_right():
	x = player.xcor()
	x += playerspeed
	if x > 280:
		x = 280
	player.setx(x)

def move_down():
	y = player.ycor()
	y -= playerspeed
	if y < - 280:
		y = - 280
	player.sety(y)

def move_up():
	y = player.ycor()
	y += playerspeed
	if y > 280:
		y = 280
	player.sety(y)



def fire_bullet():
	global bulletstate
	if bulletstate == "ready":
		os.system("afplay laser.wav&")
		bulletstate = "fire"
		x = player.xcor()
		print("y coord: " + str(x))
		y = player.ycor() + 10
		bullet.setposition(x, y)
		bullet.showturtle()

def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 15:
		return True
	else:
		return False

turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(move_down, "Down")
turtle.onkey(move_up, "Up")
turtle.onkey(fire_bullet, "space")

#Main main game loop
while True:

	for enemy in enemies:
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)

		if enemy.xcor() > 280:
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			enemyspeed *= -1

		if enemy.xcor() < -280:
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			enemyspeed *= -1

		if isCollision(bullet, enemy):
			os.system("afplay explosion.wav&")
			bullet.hideturtle()
			bulletstate = "ready"
			bullet.setposition(0, -500)
			x = random.randint(-200, 200)
			#y = random.randint(100, 250)
			y = 280
			enemy.setposition(x, y)
			score += 10
			scorestring = "Score: %s" %score
			score_pen.clear()
			score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))


			if score %50 == 0:
				for i in range(number_enemies2):
					enemies.append(turtle.Turtle())

				for enemy in enemies:
					enemy.color("orange")
					enemy.shape("invader.gif")
					enemy.penup()
					enemy.speed(0)
					x = random.randint(-200, 200)
					y = random.randint(100, 250)
					enemy.setposition(x, y)
					#enemyspeed += 1
 

		if isCollision(player, enemy):
			os.system("afplay explosion.wav&")
			player.hideturtle()
			enemy.hideturtle()
			print ("Game Over fool")
			
			break

	if bulletstate == "fire":
		y = bullet.ycor()
		y += bulletspeed
		bullet.sety(y)
	
	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletstate = "ready"

delay = raw_input

#to run in xterm: python3 turtleinvaders.py
#CONTROLS: Spacebar: shoot, ARROW KEYS = move

