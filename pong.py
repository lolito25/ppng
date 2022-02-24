import turtle

#Ventana 
ventana = turtle.Screen()
ventana.title("Pong")
ventana.bgcolor("black")
ventana.setup(width= 800, height= 600)
ventana.tracer(0)

#marcador
marcador1 = 0
marcador2 = 0

#Players1
jugador1 = turtle.Turtle()
jugador1.speed(0)
jugador1.shape("square")
jugador1.color("white")
jugador1.penup()
jugador1.goto(-350,0)
jugador1.shapesize(stretch_wid = 5, stretch_len=1)

#Player2
jugador2 = turtle.Turtle()
jugador2.speed(0)
jugador2.shape("square")
jugador2.color("white")
jugador2.penup()
jugador2.goto(350,0)
jugador2.shapesize(stretch_wid= 5 , stretch_len= 1)

#Ball
pelota =turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)
pelota.dx = 3
pelota.dy = 3

#linea-division
linea = turtle.Turtle()
linea.color("white")
linea.goto(0,400)
linea.goto(0,-400)

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("JUGADOR1: 0   JUGADOR2: 0 ", align ="center", font=("Courier", 24 , "normal"))

#funciones del jugador1
def jugador1_up():
    y = jugador1.ycor()
    y += 20
    jugador1.sety(y)

#conectando el teclado hacia arriba del player1
ventana.listen()
ventana.onkeypress (jugador1_up, "w")

def jugador1_down():
    y = jugador1.ycor()
    y -= 20
    jugador1.sety(y)

#control hacia abajo del jugador1
ventana.listen()
ventana.onkeypress(jugador1_down, "s")


#funciones del jugador2
def jugador2_up():
    y = jugador2.ycor()
    y += 20
    jugador2.sety(y)

ventana.listen()
ventana.onkeypress(jugador2_up, "Up")

def jugador2_down():
    y = jugador2.ycor()
    y -= 20
    jugador2.sety(y)

ventana.listen()
ventana.onkeypress(jugador2_down, "Down")



while True:
    ventana.update()

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    #limites de bordes
    if pelota.ycor() > 290 :
        pelota.dy *= -1
    if pelota.ycor() < -290 :
        pelota.dy *= -1 
    
    #bordes derecha e izquierda
    if pelota.xcor()> 390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcador1 += 1
        pen.clear()
        pen.write("JUGADOR1: 0 {}   JUGADOR2: 0  {}".format(marcador1 , marcador2), align ="center", font=("Courier", 24 , "normal"))

    if pelota.xcor()< -390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcador2 += 1
        pen.clear()
        pen.write("JUGADOR1: 0   JUGADOR2: 0 ", align ="center", font=("Courier", 24 , "normal"))

    if ((pelota.xcor() > 340 and pelota.xcor() < 350)
        and (pelota.ycor() < jugador2.ycor() + 50 
        and pelota.ycor() > jugador2.ycor() - 50)):
        pelota.dx *= -1

    if ((pelota.xcor() < -340 and pelota.xcor() > -350)
        and (pelota.xcor() > jugador1.xcor() + 50 
        and pelota.ycor() > jugador1.ycor() - 50)):
        pelota.dx*= -1






