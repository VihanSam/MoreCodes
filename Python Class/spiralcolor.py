import turtle
T = turtle.Pen()
turtle.bgcolor("black")
name = turtle.textinput("Your name","Enter your name")
for x in range(100):
    T.pencolor("light blue")
    T.forward(x*4)
    T.write(name,font = ("Arial",int(37),"bold"))
    T.left(92)
