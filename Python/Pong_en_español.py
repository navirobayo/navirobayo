# "Pong en español" // Código estudiado y traducido por Ivan Robayo @ivanrobayo667 - Colombia 8/04/2022.
# Tutorial tomado de freecodecamp.org (Christian Thompson.)

import turtle

wn = turtle.Screen()
wn.title = ("EJERCICIO: Pong en español. Escrito en Python. Código fuente en GitHub @ivanrobayo667")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Puntaje (Variable)

score_a = 0 
score_b = 0 

# Paleta A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paleta B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Bola

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5

# Lápiz (Tablero de Puntaje)

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Jugador A: 0 Jugador B: 0".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

# Funciones (Posición paletas)

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20 
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20 
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20 
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20 
    paddle_b.sety(y)

# Controles

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.listen()
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Mecanismo principal 

while True:
    wn.update()


    # Movimiento Bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Bordes 
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1 
        score_a += 1
        pen.clear()
        pen.write("Jugador A: {} Jugador B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1 
        score_b += 1
        pen.clear()
        pen.write("Jugador A: {} Jugador B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paletas y colisiones

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60):
        ball.setx(-340)
        ball.dx *= -1

# Fin. 
# "Pong en español"  Código estudiado y traducido por Ivan Robayo @ivanrobayo667 - Colombia 8/04/2022.
# Tutorial tomado de freecodecamp.org (Christian Thompson.) 
