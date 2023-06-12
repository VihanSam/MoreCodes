import turtle
T = turtle.Pen()
turtle.bgcolor("white")
C = ["Orange","Purple","Pink","Blue"]
for x in range(100):
    T.pencolor(C[x%4])
    T.circle(x)
    T.left(91)
