import turtle as t
t.speed(1000000)

# Task: Create a face using a turtle
# Draw head
# Draw eyes
# Draw nose
# Draw Checks
# Draw mouth
# Move Function
def myMove(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def myCircle(sz, c):
    t.fillcolor(c)
    t.begin_fill()
    t.circle(sz)
    t.end_fill()

t.circle(100)
myMove(-50, 100)
myCircle(18, "red")
myMove(-50, 102)
myCircle(16, "orange")
myMove(-50, 104)
myCircle(14, "yellow")
myMove(-50, 106)
myCircle(12, "lightgreen")
myMove(-50, 108)
myCircle(10, "green")
myMove(-50, 110)
myCircle(8, "lightblue")
myMove(-50, 112)
myCircle(6, "blue")
myMove(-50, 114)
myCircle(4, "purple")
myMove(-50, 116)
myCircle(2, "darkblue")

myMove(50, 100)
myCircle(18, "darkblue")
myMove(50, 102)
myCircle(16, "purple")
myMove(50, 104)
myCircle(14, "blue")
myMove(50, 106)
myCircle(12, "lightblue")
myMove(50, 108)
myCircle(10, "green")
myMove(50, 110)
myCircle(8, "lightgreen")
myMove(50, 112)
myCircle(6, "yellow")
myMove(50, 114)
myCircle(4, "orange")
myMove(50, 116)
myCircle(2, "red")

t.fillcolor("white")
t.begin_fill()
myMove(43, 108)
t.left(45)
t.forward(30)
t.left(90)
t.forward(5)
t.left(90)
t.forward(30)
t.left(90)
t.forward(5)
t.end_fill()

t.fillcolor("red")
t.begin_fill()
myMove(63, 111)
t.left(180)
t.forward(30)
t.left(90)
t.forward(5)
t.left(90)
t.forward(30)
t.left(90)
t.forward(5)
t.end_fill()

t.fillcolor("blue")
t.begin_fill()
myMove(-63, 125)
t.left(270)
t.forward(30)
t.left(90)
t.forward(5)
t.left(90)
t.forward(30)
t.left(90)
t.forward(5)
t.end_fill()

t.fillcolor("red")
t.begin_fill()
myMove(-58, 105)
t.left(180)
t.forward(30)
t.left(90)
t.forward(5)
t.left(90)
t.forward(30)
t.left(90)
t.forward(5)
t.end_fill()

myMove(-12.5,55)
myCircle(20,"red")
t.forward(50)
t.left(120)
t.forward(50)
t.left(120)
t.forward(50)


t.ht()
t.Screen().exitonclick()