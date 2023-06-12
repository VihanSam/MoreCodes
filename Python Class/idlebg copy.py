import turtle
T = turtle.Pen()
colors = ["light blue", "black", "purple", "red"]
turtle.bgcolor("white")
for x in range(500):
    T.pencolor(colors[x%4])
    T.circle(x)
    T.left(90)
