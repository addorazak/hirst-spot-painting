# import colorgram
import random
import turtle
# Extract colors from the image
# colors = colorgram.extract('image.jpg', 30)
#
# # print(colors)
# color_bank = []

# for color in colors:
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#     new_color = (r, g, b)
#     color_bank.append(new_color)

# print(color_bank)

# List of rgb colors generated from the code above
color_list = [(235, 229, 99), (18, 114, 167),
              (163, 80, 48), (208, 159, 92), (186, 13, 63), (131, 180, 201), (230, 78, 49), (36, 137, 84), (7, 35, 89),
              (148, 163, 37), (76, 41, 22), (166, 48, 91), (113, 186, 165), (223, 120, 149), (20, 169, 208),
              (62, 159, 92), (215, 72, 118), (8, 94, 52), (238, 163, 191), (95, 21, 68), (147, 205, 223), (213, 223, 9),
              (12, 87, 107), (247, 170, 146), (11, 46, 125), (160, 211, 188)
              ]

turtle.colormode(255)
raz = turtle.Turtle()
screen = turtle.Screen()

raz.speed('fastest')
raz.penup()
raz.hideturtle()

raz.setheading(225)
raz.forward(300)
raz.setheading(0)
num_of_dots = 101

for dot_count in range(1, num_of_dots):
    raz.dot(20, random.choice(color_list))
    raz.forward(50)

    if dot_count % 10 == 0:
        raz.setheading(90)
        raz.forward(50)
        raz.setheading(180)
        raz.forward(500)
        raz.setheading(0)


screen.exitonclick()
