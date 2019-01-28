import turtle
import time
import random

screen = turtle.Screen()
screen.title("snake")
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer = (0)

head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color("blue")

head.penup()
head.goto(0, 0)
head.direction = 'stop'

delay = 0.1
speed = 20
def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y +speed)
    elif head.direction == 'down':
        y = head.ycor()
        head.sety(y - speed)
    elif head.direction == 'left':
        x = head.xcor()
        head.setx(x - speed)
    elif head.direction == 'right':
        x = head.xcor()
        head.setx(x + speed)

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

screen.listen()
screen.onkeypress(goUp, 'w')
screen.onkeypress(goDown, 's')
screen.onkeypress(goLeft, 'a')
screen.onkeypress(goRight, 'd')

food = turtle.Turtle()
food.speed(0) 
food.shape("circle") 
food.color("red")
food.penup()
food.goto(0 ,100)

snakeBody = []

while True:
    screen.update()
    time.sleep(delay)
   
    #print(speed)
    
    if head.distance(food) < 20: 
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        
        food.goto(x, y)
    
        newBodyPart = turtle.Turtle()
        newBodyPart.speed(0)
        newBodyPart.shape('square')
        newBodyPart.color('purple')
        newBodyPart.penup()
        snakeBody.append(newBodyPart)
        
    for index in range(len(snakeBody) - 1, 0, -1):
        x = snakeBody[index - 1].xcor()
        y = snakeBody[index - 1].ycor()
    
        snakeBody[index].goto(x, y)
    
    if len(snakeBody) > 0:
        x = head.xcor()
        y = head.ycor()
    
        snakeBody[0].goto(x, y)
    move()    
screen.mainloop()



