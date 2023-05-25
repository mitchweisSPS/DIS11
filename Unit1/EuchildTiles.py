import turtle as t
t.speed(20)

floorwidth = 345
floorlength = 150
numberOfTilesX = 0
numberOfTilesY = 0
tileLength = 0
startingX = 0
startingY = 0
a = 345
b = 150
c = 0
def euchild(a,b):
    c = 1
    while c != 0:
        c = a % b
        a = b
        b = c
    return(a)

tileLength = euchild(345,150)
print(tileLength)
numberOfTilesX = floorwidth / tileLength
numberOfTilesY = floorlength / tileLength
print(numberOfTilesX)
print(numberOfTilesY)

def myTile():
        t.fillcolor("red")
        t.begin_fill()
        for i in range(4):
            t.forward(tileLength)
            t.left(90)
        t.penup()
        t.goto(startingX + tileLength, startingY)
        t.pendown()
        t.end_fill()

myTile()

t.ht()
t.Screen().exitonclick()
