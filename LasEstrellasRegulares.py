
import turtle

turtle.shape("turtle")

def EstrellasRegulares(n):

    ws = turtle.Screen()
    geekyTurtle = turtle.Turtle('turtle')

    if n%2!=0:
        for i in range(n):
            geekyTurtle.forward(200)
            geekyTurtle.right(180-(180/n))

    else:
        coords = []
        for x in range(n):
            turtle.penup()
            coords.append(turtle.pos())
            turtle.circle(100,(360/n))
        for y in range(0,len(coords)):
            if y%2==0:
                turtle.pendown()
                turtle.goto(coords[y][0], coords[y][1])
            else:
                continue
        turtle.goto(coords[0][0], coords[0][1])
        turtle.penup()
        for z in range(0, (len(coords)+1)):
            if z%2!=0:
                turtle.goto(coords[z][0],coords[z][1])
                turtle.pendown()
            else:
                continue
        turtle.goto(coords[1][0], coords[1][1])
    return
