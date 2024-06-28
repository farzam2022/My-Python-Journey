# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('hh3.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import turtle as tim
import random

tim.colormode(255)
t = tim.Turtle()
t.speed("fastest")
color_list= [(131, 146, 205), (182, 42, 80), (220, 50, 82), (43, 175, 94), (224, 155, 101), (25, 109, 131), (144, 23, 43), (180, 222, 233), (34, 58, 41), (7, 62, 168), (52, 125, 80), (70, 200, 197), (48, 199, 202), (207, 137, 151), (139, 19, 18), (129, 116, 196), (19, 91, 101), (31, 88, 81), (186, 180, 213), (147, 213, 200), (219, 173, 180), (202, 201, 156), (100, 19, 13), (142, 74, 67), (228, 174, 164), (195, 88, 87), (158, 210, 216)]
t.penup()
t.hideturtle()
t.setheading(225)
t.forward(300)
t.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots+1):
    t.dot(20, random.choice(color_list))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

s = tim.Screen()
s.exitonclick()