import turtle as t
t.speed(20)

def myMove(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def myCircle(sz):
    t.circle(sz)

f1 = 0
f2 = 1
sum = 0
width = 0
numberOfBubbles = 0
x = -300

while numberOfBubbles < 15:
    sum = f1 + f2
    f2 = f1
    f1 = sum
    width = sum
    numberOfBubbles += 1
    myMove(x, 0)
    myCircle(width)
    x = x + 50
    t.write(sum)

t.ht()
t.Screen().exitonclick()
