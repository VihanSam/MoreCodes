import turtle
T = turtle.Pen()
turtle.bgcolor("white")
sides = 100
colors = ["Blue","Orange","Purple","Red","Green","Pink","Aqua","Cyan","Yellow","Brown"]
for x in range (360):
    T.pencolor(colors[x%10])
    T.forward(x * 3/sides + x)
    T.left(360/ sides + 1)
    T.width(x*sides/200)
    T.left(90)
    T.forward(50)
    T.backward(20)
    

#List of how it look from the python picture with only 2 sides! :)
#A Spiral stair case
#A Mustache
#A Peacok
#A 180 Degrees
#
#A Weird mustache 


#Triangle #Sides = 3
#Circle #Sides = 10
#Normal #Sides = 6
#Mustache #Sides = 2
#BIG SQUARE #Sides = 100 !
#Spike Star #Sides = 5
