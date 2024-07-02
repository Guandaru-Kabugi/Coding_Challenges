import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")
tim.color("blue")
tim.pensize(10)
tim.speed("fastest")

def random_colors ():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    my_tuple = (r,g,b)
    return my_tuple
counting = 0
directions = [0,90,180,270]

for _ in range (200):
    tim.pencolor(random_colors())
    tim.forward(30)
    tim.setheading(random.choice(directions))








screen = Screen()
screen.exitonclick()