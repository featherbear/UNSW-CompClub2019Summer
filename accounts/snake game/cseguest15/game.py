import turtle
import time
import random

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup()
head.goto(0,0)
head.direction = "stop"
delay = 0.08
speed = 20

def move():
  if head.direction == "up":
    y = head.ycor()
    head.sety(y+speed)
  if head.direction == "down":
    y = head.ycor()
    head.sety(y-speed)
  if head.direction == "right":
    x = head.xcor()
    head.setx(x+speed)
  if head.direction == "left":
    x = head.xcor()
    head.setx(x-speed)

def goUp():
  if head.direction != "down":
    head.direction = "up"
def goDown():
  if head.direction != "up":
    head.direction = "down"
def goRight():
  if head.direction != "left":
    head.direction = "right"
def goLeft():
  if head.direction != "right":
    head.direction = "left"

def gameStop():
  time.sleep(1)
  head.goto(0,0)
  head.direction = "stop"
  
  for part in snakeBody:
    part.goto(1000,1000)
    
  snakeBody.clear()
  pen.clear()
  score = 0
  pen.write("Score: " + str(score) + " ---- High Score: " + str(highScore), align="center", font=("Courier", 24, "normal"))


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

food2 = turtle.Turtle()
food2.speed(0)
food2.shape("circle")
food2.color("yellow")
food2.penup()
food2.goto(0,200)

score = 0 
highScore = 0

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: " + str(score) + " ---- High Score: " + str(highScore), align="center", font=("Courier", 24, "normal"))

snakeBody = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
while True:
  screen.update()
  time.sleep(delay)
  for part in snakeBody:
    if part.distance(head) < 1:
      score = 0
      gameStop()
     
    
  if head.distance(food) < 20:
    x = random.randint(-270,270)
    y = random.randint(-270,270)
    food.goto(x,y)
    
    
    newBodyPart = turtle.Turtle()
    newBodyPart.speed(0)
    newBodyPart.shape("square")
    new = random.randint(0,5)
    newBodyPart.color(colors[new])
    newBodyPart.penup()
    snakeBody.append(newBodyPart)
    
    score = score + 1
    if score > highScore:
      highScore = score
    pen.clear()
    pen.write("Score: " + str(score) + " ---- High Score: " + str(highScore), align="center", font=("Courier", 24, "normal"))
    
  if len(snakeBody) == 5:
    newBodyPart.color(colors[new])
    
  if head.distance(food2) < 20:
    a = random.randint(-270,270)
    b = random.randint(-270,270)
    food2.goto(a,b)
    
    
    newBodyPart = turtle.Turtle()
    newBodyPart.speed(0)
    newBodyPart.shape("square")
    newBodyPart.color("pink")
    newBodyPart.penup()
    snakeBody.append(newBodyPart)
    
    score = score + 1
    if score > highScore:
      highScore = score
    pen.clear()
    pen.write("Score: " + str(score) + " ---- High Score: " + str(highScore), align="center", font=("Courier", 24, "normal"))

  for index in range(len(snakeBody) -1, 0, -1):
    x = snakeBody[index-1].xcor()
    y = snakeBody[index-1].ycor()
    snakeBody[index].goto(x,y)
  
  if len(snakeBody) > 0:
    x = head.xcor()
    y = head.ycor()
    snakeBody[0].goto(x,y)
  
  if head.xcor() > 290 or head.xcor() < -290:
    score = 0
    gameStop()
  
  if head.ycor() >290 or head.ycor() < -290:
    score = 0
    gameStop()

      
  move()





screen.mainloop()
