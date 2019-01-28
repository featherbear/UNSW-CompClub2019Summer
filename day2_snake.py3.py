import turtle
import random

multiplayer = True

boardSize = 30
delay = 0.05

# ()
radius = (int(boardSize / 2))
moveDistance = (20)
blockWidth = (20)
dim = (boardSize * blockWidth)
border = (dim / 2)
scores = {}


screen = turtle.Screen()
screen.title("snek")
screen.bgcolor("black")
screen.setup(width = dim, height = dim)

screen.tracer(0)  # turn off animation


def randomPos():
    return random.randint(-radius + 1, radius - 1) * blockWidth, random.randint(-radius + 1, radius - 1) * blockWidth


class Snake():
    parts = []
    color = "green"
    direction = ""

    @property
    def head(self):
        return self.parts[0]

    def _newBlock(self):
        t = turtle.Turtle()
        t.speed(0)
        t.shape("square")
        t.color(self.color)
        t.penup()
        return t

    def _add(self):
        self.parts.append(self._newBlock())

    def __init__(self, color = None):
        self.parts = []
        self.color = color or "green"
        self.direction = ""

        self._add()
        self.head.goto(randomPos())

        self.oldX = None
        self.oldY = None

    def move(self):
        self.oldX = self.head.xcor()
        self.oldY = self.head.ycor()

        # move previous body
        for n in range(len(self.parts) - 1, 0, -1):
            x = self.parts[n - 1].xcor()
            y = self.parts[n - 1].ycor()
            self.parts[n].goto(x, y)

        if self.direction == "up":
            y = self.head.ycor() + moveDistance
            if y > border - blockWidth: y = -border
            self.head.sety(y)
        elif self.direction == "down":
            y = self.head.ycor() - moveDistance
            if y < -border + blockWidth: y = border
            self.head.sety(y)
        elif self.direction == "left":
            x = self.head.xcor() - moveDistance
            if x < -border + blockWidth: x = border
            self.head.setx(x)
        elif self.direction == "right":
            x = self.head.xcor() + moveDistance
            if x > border - blockWidth: x = -border
            self.head.setx(x)

    def goUp(self):
        if self.direction != "down":
            self.direction = "up"

    def goDown(self):
        if self.direction != "up":
            self.direction = "down"

    def goLeft(self):
        if self.direction != "right":
            self.direction = "left"

    def goRight(self):
        if self.direction != "left":
            self.direction = "right"

    def grow(self):
        tail = self._newBlock()
        tail.goto(self.oldX, self.oldY)
        self.parts.append(tail)

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("white")
food.penup()
food.goto(randomPos())
import time
food.last = int(time.time())

snakes = []

## Player One
snakes.append(Snake())
scores[snakes[0]] = 0
screen.onkeypress(snakes[0].goUp, 'w')
screen.onkeypress(snakes[0].goDown, 's')
screen.onkeypress(snakes[0].goLeft, 'a')
screen.onkeypress(snakes[0].goRight, 'd')

## Player Two
if multiplayer:
    snakes.append(Snake("blue"))
    scores[snakes[1]] = 0
    screen.onkeypress(snakes[1].goUp, 'Up')
    screen.onkeypress(snakes[1].goDown, 'Down')
    screen.onkeypress(snakes[1].goLeft, 'Left')
    screen.onkeypress(snakes[1].goRight, 'Right')

pen = turtle.Turtle()

def updateScore():
    pen.clear()
    pen.goto(0, 0)
    pen.write("Score: " + "-".join(map(str, list(scores.values()))), True, "center", ("Arial", 12, "normal"))

pen.speed()
pen.color("grey")
pen.penup()
pen.hideturtle()
updateScore()


screen.listen()

def gameLoop():
    while True:
        if int(time.time()) - food.last > 10:
            food.goto(randomPos())
            food.last = int(time.time())
        for n in range(len(snakes)):
            snek = snakes[n]

            snek.move()
            headPos = snek.head.pos()
            for p in snek.parts[1:]:
                if headPos == p.pos():
                    print("RIP")
                    return

            for s in range(len(snakes)):
                if s == n: continue
                for part in snakes[s].parts:
                    if headPos == part.pos():
                        print("RIP")
                        return

            if food.distance(snek.head) < 1:
                scores[snek] += r1
                updateScore()
                food.goto(randomPos())
                food.last = int(time.time())
                snek.grow()

        # check for head collision
        screen.update()
        time.sleep(delay)

gameLoop()
screen.mainloop()