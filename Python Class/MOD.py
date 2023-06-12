import turtle
T = turtle.Pen()
turtle.bgcolor("black")
colors = ["light blue","yellow","red","purple","pink"]
name = turtle.textinput("Your name","Enter your name")
for x in range(100):
    T.pencolor(colors[x%5])
    T.penup()
    T.forward(x*4)
    T.pendown()
    T.write(name,font = ("Arial",int((x+4)/4),"bold"))
    T.left(69)
