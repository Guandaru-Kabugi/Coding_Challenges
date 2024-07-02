from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()
screen.colormode(255)
timmy.shape("turtle")
timmy.speed("fastest")
angle = [0, 90, 180, 270]


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    colour = (red, green, blue)
    return colour


def draw_circles(num_of_gap):
    for _ in range(int(360 / num_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.right(num_of_gap)


draw_circles(10)

screen.exitonclick()