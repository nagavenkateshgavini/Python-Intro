import turtle

t1 = turtle.Turtle()
t1.shape("turtle")
t1.speed(0)
t1.width(3)
t1.color("yellow", "red")

t2 = turtle.Turtle()
t2.shape("turtle")
t2.speed(0)
t2.width(3)
t2.color("blue", "orange")

t3 = turtle.Turtle()
t3.shape("turtle")
t3.speed(0)
t3.width(3)
t3.color("red", "blue")

t1.penup()
t1.goto(150, 150)
t1.pendown()

t2.penup()
t2.goto(-150, -150)
t2.pendown()

t3.penup()
t3.goto(-150, 150)
t3.pendown()

def draw_box(t):
    t.begin_fill()
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.end_fill()
    t.right(10)

turts = [t1, t2, t3]

for a in range(36):
    for petal in turts:
        draw_box(petal)
    
    
