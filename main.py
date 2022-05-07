# simple pong_Game

import turtle as t
import winsound as w


wn = t.Screen()
wn.setup(width=800, height=600)
wn.bgcolor("black")
wn.tracer(0)
wn.title("PONG by Bibin")

#scoring
score_a = 0
score_b = 0

# paddle A
paddle_a = t.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = t.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
# Ball
ball = t.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2
#pen
pen=t.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("PLAYER A:0  PLAYER B:0",align="center",font=("courier",24,"normal"))


# function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    if paddle_a.ycor()>=250:
        paddle_a.ycor(250)
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    if paddle_a.ycor() <= -250:
        paddle_a.ycor(-250)
    paddle_a.sety(y)



def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    if paddle_b.ycor()>=250:
        paddle_b.ycor(250)
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    if paddle_b.ycor() <= -250:
        paddle_b.ycor(-250)
    paddle_b.sety(y)

# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down,"Down")
# main Game_Loop
while True:
    wn.update()


    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Border Checking

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        w.PlaySound("hit.wav", w.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        w.PlaySound("hit.wav", w.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("PLAYER A:{}  PLAYER B:{}".format(score_a,score_b), align="center", font=("courier", 24, "normal"))
        w.PlaySound("hit.wav", w.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("PLAYER A:{}  PLAYER B:{}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))
        w.PlaySound("hit.wav", w.SND_ASYNC)
    #paddle and ball collisions

    if ball.xcor() > 340 and ball.xcor() <350 and (ball.ycor()< paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        w.PlaySound("hit1.wav", w.SND_ASYNC)

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor()< paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        w.PlaySound("hit1.wav", w.SND_ASYNC)