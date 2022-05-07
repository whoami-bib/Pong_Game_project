#simple pong_Game

import turtle as t
wn=t.Screen()
wn.setup(width=800,height=600)
wn.bgcolor("black")
wn.tracer(0)
wn.title("PONG by Bibin")

#paddle A
paddle_a=t.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b=t.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)
#Ball
ball=t.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)


while True:
    wn.update()