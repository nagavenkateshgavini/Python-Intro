import turtle
import random

screen = turtle.Screen()
turtle.setup(1024, 768)
turtle.bgcolor("#FFFFE0")

t1 = turtle.Turtle()
t1.speed(0)
t1.shape("turtle")
t1.width(3)
t1.color("red")

for side in range(4):
    t1.forward(100)
    t1.stamp()
    t1.right(90)
