import turtle
import os
import random
import math


#screen
wn = turtle.Screen()
wn.title("PingPangPong")
wn.bgcolor("black")
wn.setup(width = 1.0, height = 1.0)

#Shapes
turtle.register_shape("elon2.gif")
turtle.register_shape("elon2.gif")

#bordure
bordure = turtle.Turtle()
bordure.penup()
bordure.color("white")
bordure.pensize(3)
bordure.ht()
bordure.setposition(-500, 300)
bordure.speed(5)
def bordure1():
        bordure.pendown()
        bordure.fd(1000)
        bordure.pu()
        bordure.setposition(-500,-300)
        bordure.pd()
        bordure.fd(1000)

def filet():
    bordure.pensize(1)
    bordure.setposition(0, -300)
    bordure.setheading(90)
    for i in range (12):
        bordure.fd(26)
        bordure.penup()
        bordure.fd(26)
        bordure.pendown()

bordure1()
filet()


#Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ballspeed = 8
ballheading = random.randint(1,360)
ball.penup()
ball.setheading(ballheading)
ball.speed(0)

#Player 1
player1 = turtle.Turtle()
player1.shape("elon2.gif")
player1.turtlesize(2,2)
player1.color("white")
player1.penup()
player1.setposition(-520, 0)
player1.speed(0)
playerspeed = 50

#Player 2
player2 = turtle.Turtle()
player2.shape("elon2.gif")
player2.shapesize(5,5)
player2.color("white")
player2.penup()
player2.setposition(520, 0)
player2.speed(0)
playerspeed = 50

#Player 1 Movement
def up():
        y = player1.ycor()
        y += playerspeed
        if y < 270:
                player1.sety(y)

def down():
        y = player1.ycor()
        y -= playerspeed
        if y > -270:
                player1.sety(y)               
#Player 2 movement
def up1():
        y = player2.ycor()
        y += playerspeed
        if y < 280:
                player2.sety(y)

def down1():
        y = player2.ycor()
        y -= playerspeed
        if y > -280:
                player2.sety(y)
#Speed hack
def hack():
        global ballspeed
        if ballspeed == 8:
                ballspeed = 20
        elif ballspeed == 20:
                ballspeed = 8

def start():
        ballheading = random.randint(1,360)
        ball.setposition(0, 0)
        ball.setheading(ballheading)


def distance(t1,t2):
        distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
        if distance < 45:
                t2.right(91)

def angle():
        print(ball.heading())



#We assign z/s to move the player 1
turtle.listen()
turtle.onkey(up, "z")
turtle.onkey(down,"s")
#We assign up and down arrow to move the player 2
turtle.onkey(up1, "Up")
turtle.onkey(down1,"Down")
#SpeedHack
turtle.onkey(hack, "m")
#Restart
turtle.onkey(start,"p")
#Print the Ball heading
turtle.onkey(angle, "l")
#Player 2 score's
Score1 = 0
s1 = turtle.Turtle()
s1.speed(0)
s1.ht()
s1.color("white")
s1.pu()
s1.setposition(-250, 250)
s1.write(Score1, font=("Arial", 44, "normal"))
#Player 2 score's
Score2 = 0
s2 = turtle.Turtle()
s2.speed(0)
s2.ht()
s2.color("white")
s2.pu()
s2.setposition(250, 250)
s2.write(Score1, font=("Arial", 44, "normal"))

#Mainloop
while True:
        ball.fd(ballspeed)
        degree = ball.heading()
        y = ball.ycor()
        x = ball.xcor()
#We define the border colision 
        if y > 279 or y < -279:
                 ball.right(91)
#We define Loose              
        if x > 520:
                ballheading = random.randint(1,360)
                Score1 += 1
                s1.clear()
                s1.write(Score1, font=("Arial", 44, "normal"))
                start()
        if x < -520:
                ballheading = random.randint(1,360)
                Score2 += 1
                s2.clear()
                s2.write(Score2, font=("Arial", 44, "normal"))
                start()

#Colision beetween players and ball                
        distance(player1,ball)
        distance(player2,ball)

turtle.mainloop()
