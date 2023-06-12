import turtle
T = turtle.Pen()
turtle.bgcolor("black")
C = ["Orange","Purple","Pink","Blue"]
for x in range(100):
    T.pencolor(C[x%4])
    T.forward(x)
    T.left(10)
#How it looks
#Spiral
#Glob
#Blob
#
