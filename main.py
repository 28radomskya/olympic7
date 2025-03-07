import turtle


screen = turtle.Screen()
screen.screensize( 500,  500)
t = turtle.Turtle()
screen.bgcolor("tan")
t.speed(0)

t.penup()
t.goto(-80,15)
t.pendown()
t.pencolor("blue")
t.circle(35)

t.penup()
t.goto(0,15)
t.pendown()
t.pencolor("black")
t.circle(35)

t.penup()
t.goto(80,15)
t.pendown()
t.pencolor("red")
t.circle(35)

t.penup()
t.goto(-40,-15)
t.pendown()
t.pencolor("yellow")
t.circle(35)

t.penup()
t.goto(40,-15)
t.pendown()
t.pencolor("green")
t.circle(35)

t.penup()
t.goto( 0, 100)
t.pendown()
t.pencolor("purple")
t.write("Winter Olympics",font = ("arial",30,"normal"),align="center")

t.penup()
t.goto( 0, -100)
t.pendown()
t.pencolor("purple")
t.write("2026",font = ("arial",30,"normal"),align="center")

turtle.done()