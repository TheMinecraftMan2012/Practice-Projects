import turtle

def triangle():
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)

turtle.penup()
turtle.goto(-190, 100)
turtle.pendown()
turtle.color("brown")
turtle.begin_fill()
turtle.forward(280)
triangle()
turtle.end_fill()

turtle.penup()
turtle.goto(-10, 100)
turtle.pendown()
turtle.color("brown")
turtle.begin_fill()
triangle()
turtle.end_fill()

turtle.penup()
turtle.goto(-110, 100)
turtle.pendown()
turtle.color("brown")
turtle.begin_fill()
triangle()
turtle.end_fill()

turtle.penup()
turtle.goto(-210, 100)
turtle.pendown()
turtle.color("brown")
turtle.begin_fill()
triangle()
turtle.end_fill()

turtle.colormode(255)

turtle.penup()
turtle.goto(90, 150)
turtle.pendown()
turtle.color(255, 204, 0)
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

turtle.penup()
turtle.goto(-100, -80)
turtle.color("darkgreen")
turtle.pendown()
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

turtle.penup()
turtle.goto(-80, -120)
turtle.color("darkgreen")
turtle.pendown()
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

turtle.penup()
turtle.goto(-120, -120)
turtle.color("darkgreen")
turtle.pendown()
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

turtle.penup()
turtle.goto(-120, -120)
turtle.color("brown")
turtle.pendown()
turtle.begin_fill()
for i in range(2):
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.goto(70,-70)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
for i in range(4):
  turtle.forward(70)
  turtle.right(90)
turtle.end_fill()
turtle.penup()
turtle.goto(70,-70)
turtle.pendown()
turtle.color("skyblue")
turtle.begin_fill()
for i in range(3):
  turtle.forward(70)
  turtle.left(120)
turtle.end_fill()
turtle.penup()
turtle.goto(105,-70)
turtle.pendown()
turtle.color("darkblue")
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()
turtle.penup()

turtle.done()