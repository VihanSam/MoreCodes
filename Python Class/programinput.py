import turtle
T = turtle.Pen()
T.pencolor("blue")
turtle.bgcolor("black")
name = turtle.textinput("Enter your name","What is your name")
T.write(name,font = ("Arial",int(27),"bold"))
