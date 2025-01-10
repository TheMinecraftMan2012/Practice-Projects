import turtle
import random

x = 30

for i in range(5):
    x -= 30

    turtle.penup()
    turtle.goto(x, 0)
    turtle.pendown()
    turtle.colormode(255)
    turtle.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()

turtle.penup()
turtle.goto(-130, 30)
turtle.pendown()
turtle.color("black")
turtle.begin_fill()
turtle.circle(7)
turtle.end_fill()
turtle.penup()
turtle.goto(-100, 30)
turtle.pendown()
turtle.color("black")
turtle.begin_fill()
turtle.circle(7)
turtle.end_fill()
turtle.penup()

turtle.goto(-130, 50)
turtle.pendown()
turtle.left(90)
turtle.forward(50)
turtle.penup()

turtle.goto(-110, 50)
turtle.pendown()
turtle.forward(50)
turtle.penup()

turtle.done()