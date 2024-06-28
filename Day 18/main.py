import random
import turtle as t

tis = t.Turtle()
t.colormode(255)
tis.penup()
tis.setheading(90)
tis.forward(200)
tis.setheading(0)
tis.pendown()
def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tc = (r, g, b)
    return tc

tis.pensize(5)
tis.speed("fastest")

for i in range(4, 17):
    for j in range(1, i):
        tis.color(rand_color())
        tis.right(360/(i-1))
        tis.forward(100)


s=t.Screen()
s.exitonclick()