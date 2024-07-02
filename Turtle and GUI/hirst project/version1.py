import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(234, 35, 108), (237, 74, 34), (154, 27, 61), (6, 148, 94), (215, 229, 234), (234, 168, 39), (183, 158, 45), (26, 126, 194), (43, 191, 230), (85, 27, 92), (253, 223, 0), (125, 193, 73), (241, 219, 61), (180, 40, 101), (65, 175, 100), (212, 131, 166), (211, 58, 29)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
for _ in range (10):
    for _ in range (10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.right(180)

screen = t.Screen()
screen.exitonclick()

# import colorgram
# colors = colorgram.extract('Turtle and GUI/hirst project/image.jpg', 20)
# color_list = []
# for color in colors:
#     rgb = color.rgb
#     color_tuple = tuple(rgb)
#     color_list.append(color_tuple)
# print(color_list)