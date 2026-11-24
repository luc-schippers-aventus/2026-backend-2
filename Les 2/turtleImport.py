import turtle

turtle.speed(1000)

def vierkant():
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)

def rondje():
    for i in range(360):
        turtle.forward(1)
        turtle.left(1)

def ster():
    for i in range(360):
        turtle.forward(200)
        turtle.left(151)


turtle.done()
