import turtle as t
import random

tim = t.Turtle()
directions = [0, 90, 180, 270]
t.colormode(255)

def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tc = (r, g, b)
    return tc
tim.pensize(15)

tim.speed("fastest")
for _ in range(200):
    tim.color(rand_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))




t.exitonclick()