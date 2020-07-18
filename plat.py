import turtle
import time

wn = turtle.Screen()
wn.title("Ventana")
wn.setup(width=500, height=500)
wn.bgcolor("Gray")
wn.tracer(0)

#------Bloques

bloque = turtle.Turtle()
bloque.speed(0)
bloque.shape("square")
bloque.shapesize(stretch_wid=2,stretch_len=5)
bloque.penup()
bloque.goto(-100,-220)

bloque2 = turtle.Turtle()
bloque2.speed(0)
bloque2.shape("square")
bloque2.shapesize(stretch_wid=4,stretch_len=3)
bloque2.penup()
bloque2.goto(-20,-200)

bloque3 = turtle.Turtle()
bloque3.speed(0)
bloque3.shape("square")
bloque3.shapesize(stretch_wid=6,stretch_len=4)
bloque3.penup()
bloque3.goto(50,-180)

fuego = turtle.Turtle()
fuego.speed(0)
fuego.fillcolor("Dark Red")
fuego.shape("square")
fuego.shapesize(stretch_wid=1, stretch_len=2)
fuego.penup()
fuego.goto(110,-230)

bloque4 = turtle.Turtle()
bloque4.speed(0)
bloque4.shape("square")
bloque4.shapesize(stretch_wid=10, stretch_len=1)
bloque4.penup()
bloque4.goto(140,-180)

fuego2 = turtle.Turtle()
fuego2.speed(0)
fuego2.fillcolor("Dark Red")
fuego2.shape("square")
fuego2.shapesize(stretch_wid=1, stretch_len=2)
fuego2.penup()
fuego2.goto(170,-230)

bloque5 = turtle.Turtle()
bloque5.speed(0)
bloque5.shape("square")
bloque5.shapesize(stretch_wid=13, stretch_len=3)
bloque5.penup()
bloque5.goto(220,-170)

bloquex = turtle.Turtle()
bloquex.speed(0)
bloquex.shape("triangle")
bloquex.color("yellow")
bloquex.fillcolor("green")
bloquex.shapesize(stretch_wid=1,stretch_len=1)
bloquex.penup()
bloquex.goto(220, -20)

#------Jugador

jugador = turtle.Turtle()
jugador.speed(0)
jugador.shape("circle")
jugador.fillcolor("Yellow")
jugador.penup()
jugador.goto(-230,-230)
jugador.shapesize(stretch_wid=1, stretch_len=1)
jugador.dy = -0.15
jugador.dx = -2


#------Movimiento

def jug_arriba():
    y = jugador.ycor()
    y += 60
    jugador.sety(y)

def jug_der():
    x = jugador.xcor()
    x += 10
    jugador.setx(x)

def jug_izq():
        x = jugador.xcor()
        x -= 10
        jugador.setx(x)

#------Controles

wn.listen()
wn.onkeypress(jug_arriba,"Up")
wn.onkeypress(jug_der,"Right")
wn.onkeypress(jug_izq,"Left")


while True:
    wn.update()
    if jugador.ycor() >= -230 and jugador.xcor() <= -155:
        jugador.sety(jugador.ycor() + jugador.dy)
    elif jugador.ycor() >= -190 and jugador.xcor() <= -60:
        jugador.sety(jugador.ycor() + jugador.dy)
    elif jugador.ycor() >= -150 and jugador.xcor() <= 0:
        jugador.sety(jugador.ycor() + jugador.dy)
    elif jugador.ycor() >= -110 and jugador.xcor() >= 0 and jugador.xcor() <= 90:
        jugador.sety(jugador.ycor() + jugador.dy)
    elif jugador.ycor() >= -230 and jugador.xcor() >= 90 and jugador.xcor() <= 120:
        jugador.sety(jugador.ycor() + jugador.dy)
    elif jugador.ycor() >= -70 and jugador.xcor() >= 120 and jugador.xcor() <= 155:
        jugador.sety(jugador.ycor() + jugador.dy)
    elif jugador.ycor() >=  -230 and jugador.xcor() >= 156 and jugador.xcor() <= 180:
        jugador.sety(jugador.ycor() + jugador.dy)
    elif jugador.ycor() >= -30 and jugador.xcor() >= 180:
        jugador.sety(jugador.ycor() + jugador.dy)
    if jugador.xcor() >= -160 and jugador.xcor() <= -150 and jugador.ycor() <=-195:
        jugador.setx(jugador.xcor() + jugador.dx)
    if jugador.xcor() >= -60 and jugador.xcor() <= -50 and jugador.ycor() <= -160:
        jugador.setx(jugador.xcor() + jugador.dx)
    if jugador.xcor() >= 0 and jugador.xcor() <= 10 and jugador.ycor() <= -120:
        jugador.setx(jugador.xcor() + jugador.dx)
    elif jugador.xcor() >= 90 and jugador.xcor() <= 100 and jugador.ycor() <= -125:
        jugador.setx(jugador.xcor() + jugador.dx*(-1))
    if jugador.xcor() >= 120 and jugador.xcor() <= 130 and jugador.ycor() <= -75:
        jugador.setx(jugador.xcor() + jugador.dx)
    if jugador.xcor() >= 150 and jugador.xcor() <= 160 and jugador.ycor() <= -90:
        jugador.setx(jugador.xcor() + jugador.dx*(-1))
    if jugador.xcor() >= 180 and jugador.ycor() <= -40:
        jugador.setx(jugador.xcor() + jugador.dx)
    if jugador.xcor() >= 100 and jugador.xcor() <= 180 and jugador.ycor() <= -210:
        jugador.goto(-230,-230)
    if jugador.xcor() >= 200 and jugador.xcor() <=225 and jugador.ycor() <= -5 and jugador.ycor() >= -25:
        bloquex.goto(500,500)
        turtle.write("Ganaste", move=False, align="Center",font=("Arial", 25,"normal"))
        jugador.dy = -0.4