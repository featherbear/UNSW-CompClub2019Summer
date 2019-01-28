import turtle
import time
import random
screen = turtle.Screen()
screen.title("Snake")
screen.bgcolor("pink")
screen.setup(width=1000, height=1000)
screen.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")

head2 = turtle.Turtle()
head2.speed(0)
head2.shape("square")
head2.color("black")

head.penup()
head.goto(250, 0)
head.direction = "stop"

head2.penup()
head2.goto(-250, 0)
head2.direction = "stop"

delay = 0.1
speed = 20
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

def move2():
    if head2.direction == "w":
        y = head2.ycor()
        head2.sety(y + speed)
    elif head2.direction == "s":
        y = head2.ycor()
        head2.sety(y - speed)
    elif head2.direction == "a":
        x = head2.xcor()
        head.setx(x - speed)
    elif head2.direction == "d":
        x = head2.xcor()
        head2.setx(x + speed)
            
def goUp2():
  if head2.direction != "s":
      head2.direction = "w"
        
def goDown2():
  if head2.direction != "w":
      head2.direction = "s"
        
def goLeft2():
   if head2.direction != "d":             
       head2.direction = "a"
         
def goRight2():
   if head2.direction != "a":
       head2.direction = "d"


screen.listen()
screen.onkeypress(goUp, 'Up')
screen.onkeypress(goDown, 'Down')
screen.onkeypress(goLeft, 'Left')
screen.onkeypress(goRight, 'Right')

screen.onkeypress(goUp2, 'w')
screen.onkeypress(goDown2, 's')
screen.onkeypress(goLeft2, 'a')
screen.onkeypress(goRight2, 'd')


food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0 ,100)
      
snakeBody = []

def gameStop():
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    for part in snakeBody:
        part.goto(1000, 1000)
                  
    snakeBody.clear()  
    
while True:
    screen.update()
    time.sleep(delay)


    if head.distance(food) <20:
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)
            
            newBodyPart = turtle.Turtle()
            newBodyPart.speed(0)
            newBodyPart.shape("square")
            newBodyPart.color("white")
            newBodyPart.penup()
            snakeBody.append(newBodyPart)
     
    if head2.distance(food) <20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        newBodyPart2 = turtle2.Turtle()
        newBodyPart2.speed(0)
        newBodyPart2.shape("square")
        newBodyPart2.color("black")
        newBodyPart2.penup()
        snakeBody2.append(newBodyPart2)
            
    for index in range(len(snakeBody) - 1, 0,-1):
            x = snakeBody[index - 1].xcor()
            y = snakeBody[index - 1].ycor()
            snakeBody[index].goto(x, y)
            
    if len(snakeBody) > 0:
            x = head.xcor()
            y = head.ycor()
            snakeBody[0].goto(x, y)
     
   
    move()
screen.mainloop()
