import turtle
import pygame

pygame.mixer.init()
bounce_sound = pygame.mixer.Sound("boing-2-44164.mp3")


wn = turtle.Screen()
wn.title ("pypong.game")
wn.bgcolor ("black")
wn.setup (width=800, height=500)
wn.tracer(0)

# Score
score_1 = 0
score_2 = 0

# paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

# paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = -0.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 210)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("courier", 15, "normal"))

def move_pad1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

def move_pad1_dw():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)

# keyboard binding
wn.listen()
wn.onkeypress(move_pad1_up, 'q')
wn.onkeypress(move_pad1_dw, 'p')

def move_pad2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

def move_pad2_dw():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)

wn.listen()
wn.onkeypress(move_pad2_up, "z")
wn.onkeypress(move_pad2_dw, "m")

# main game loop
while True:
    wn.update()
   
    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 240:  #top
        ball.sety(240)
        ball.dy *= -1
        bounce_sound.play()

    if ball.ycor() < -240:  #bottom
        ball.sety(-240)
        ball.dy *= -1
        bounce_sound.play()

    if ball.xcor() > 390:   #right
       ball.goto(0, 0)
       ball.dx *= -1
       score_1 += 1
       pen.clear()
       pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("courier", 15, "normal"))
       bounce_sound.play()

    if ball.xcor() < -390:  #left
       ball.goto(0, 0)
       ball.dx *= -1
       score_2 += 1
       pen.clear()
       pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("courier", 15, "normal"))
       bounce_sound.play()

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        bounce_sound.play()


    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        bounce_sound.play()


































