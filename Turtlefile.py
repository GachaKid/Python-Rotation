import turtle
turtle = turtle.Turtle()

turtle.speed('fastest')
turtle.color('crimson','black')
turtle.begin_fill()
turtle.setx(0)
turtle.sety(0)

     
def square(length, angle ):
    for t in range(4):
        turtle.forward(length)
        turtle.right(angle)
while True:
    for t in range(100):
        square(100,90)
        turtle.right(175)
        turtle.forward(100)
        turtle.up()
        turtle.back(500)
        turtle.pendown()
    break
turtle.end_fill()
turtle.penup()
turtle.setx(305)
turtle.sety(-170)
turtle.pensize(1)
turtle.color('red','orange')
turtle.begin_fill()
while True:
    for t in range(100):
        square(40,20)
        turtle.left(175)
        turtle.forward(50)      
        turtle.up()
        turtle.back(250)
        turtle.pendown()
    break
turtle.penup()
turtle.setx(-400)
turtle.pendown()

turtle.color('grey','indigo')
turtle.begin_fill()
while True:
    for t in range(100):
        square(100,90)
        turtle.left(175)
        turtle.forward(100)
        turtle.up()
        turtle.back(500)
        turtle.down()
    break
turtle.end_fill()
turtle.up()
turtle.setx(-265)
turtle.sety(-160)
turtle.pensize(2)
turtle.color('black')
turtle.begin_fill()
while True:
    for t in range(100):
        square(40,20)
        turtle.left(175)
        turtle.forward(50)      
        turtle.up()
        turtle.back(250)
        turtle.pendown()
    break
