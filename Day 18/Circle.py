import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tc = (r, g, b)
    return tc

tim.speed("fastest")
for _ in range(360, 1, -1):
    tim.color(rand_color())
    tim.circle(100)
    tim.setheading(_)




t.exitonclick()