import math
import turtle

def spiral(t, a, b):
    diff=20
    number=500
    for i in range(number):
        t.penup()
        t.fd(a+b*i*diff*math.pi/180)
        t.pendown()
        t.lt(90)
        t.fd(10)
        t.bk(10)
        t.rt(90)
        t.penup()
        t.bk(a+b*i*diff*math.pi/180)
        t.lt(diff)


bob=turtle.Turtle()
bob.speed(1000)

spiral(bob,0, 2)