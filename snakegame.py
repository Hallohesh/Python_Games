import turtle
import time
import random

delay = 0.1

score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Snake Game 4.0")
wn.bgcolor("black")
wn.setup(width=600, height=500)
wn.tracer(0)

# snake head
sh = turtle.Turtle()
sh.speed(0)
sh.shape("square")
sh.color("green")
sh.penup()
sh.goto(0, 0)

sh.direction = 'stop'

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()

segments = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 210)
pen.write("Score: 0  Highscore: 0", align='center', font=("courier", 15, "normal"))

# Functions
def move():
    if sh.direction == 'up':
        y = sh.ycor()
        sh.sety(y + 20)

    if sh.direction == 'down':
        y = sh.ycor()
        sh.sety(y - 20)

    if sh.direction == 'left':
        x = sh.xcor()
        sh.setx(x - 20)

    if sh.direction == 'right':
        x = sh.xcor()
        sh.setx(x + 20)

def go_up():
    if sh.direction != 'down':
        sh.direction = 'up'

def go_down():
    if sh.direction != 'up':
        sh.direction = 'down'

def go_left():
    if sh.direction != 'right':
        sh.direction = 'left'

def go_right():
    if sh.direction != 'left':
        sh.direction = 'right'

# Keyboard binding
wn.listen()
wn.onkeypress(go_up, 'a')
wn.onkeypress(go_down, 'l')
wn.onkeypress(go_left, 's')
wn.onkeypress(go_right, 'k')

# Game loop
while True:
    wn.update()

    # check collision with border
    if sh.xcor()>290 or sh.xcor()<-290 or sh.ycor()>240 or sh.ycor()<-240:
        time.sleep(1)
        sh.goto(0, 0)
        sh.direction = 'stop'

        # hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # clear the segments list
        segments.clear()

        # reset score
        score = 0

        # reset delay
        delay = 0.2

        # update score
        pen.clear()
        pen.write("Score: {}  Highscore: {}".format(score, high_score), align="center", font=("courier", 15, "normal"))

    # check collision with food
    if sh.distance(food) < 20:
        # move food to a random spot
        x = random.randint(-240, 240)
        y = random.randint(-240, 240)
        food.goto(x,y)

        # add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("lightgreen")
        new_segment.penup()
        segments.append(new_segment)

        # shorten the delay to speed up snake
        delay -= 0.001

        # increase score
        score +=  10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  Highscore: {}".format(score, high_score), align="center", font=("courier", 15, "normal"))

    # move segments in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # move segment 0 to head
    if len(segments) > 0:
        x = sh.xcor()
        y = sh.ycor()
        segments[0].goto(x,y)

    move()

    # check head collision with body segments
    for segment in segments:
        if segment.distance(sh) < 20:
            time.sleep(1)
            sh.goto(0, 0)
            sh.direction = ('stop')

            # hide segments
            for segment in segments:
                segment.goto(1000, 1000)

            # clear the segments list
            segments.clear()

            # reset score
            score = 0

            # reset delay
            delay = 0.2

            # update score display
            pen.clear()
            pen.write("Score: {}  Highscore: {}".format(score, high_score), align="center", font=("courier", 15, "normal"))

    time.sleep(delay)

