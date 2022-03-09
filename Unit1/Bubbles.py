import turtle as t
t.speed(20)

def myMove(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def myCircle(sz, c):
    t.fillcolor(c)
    t.begin_fill()
    t.circle(sz)
    t.end_fill()
myMove(-300, 0)
myCircle(10, "white")
myMove(-280, 0)
myCircle(10, "white")
myMove(-252.5, 0)
myCircle(20, "white")
myMove(-205, 0)
myCircle(30, "white")
myMove(-136, 0)
myCircle(40, "white")
myMove(-47, 0)
myCircle(50, "white")
myMove(62.5, 0)
myCircle(60, "white")
myMove(192.5, 0)
myCircle(70, "white")

t.ht()
t.Screen().exitonclick()
