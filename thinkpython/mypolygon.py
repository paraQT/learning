import math
import turtle

def square(t, length):

    t = turtle.Turtle()

    for i in range(4):
        t.fd(length)
        t.lt(90)


def polygon(t, length, n):

    t = turtle.Turtle()
    angle = 360 / n

    for i in range(n):
        t.fd(length)
        t.lt(angle)


def circle(t, r):

    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n

    polygon(t, n, length)


def arc(t, r, angle):
    t = turtle.Turtle()

    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)


name = input("What is the turtle's name? ")
radius = int(input("What is the radius? "))
angle = int(input("What is the angle? "))
arc(name, radius, angle)
turtle.mainloop()
