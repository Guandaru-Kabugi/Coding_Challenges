import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)
tim.shape("arrow")
tim.pensize(1)
tim.speed("fastest")

def random_colors ():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    my_tuple = (r,g,b)
    return my_tuple
def number_of_turns(angle):
    
    for _ in range (int(360/angle)):

        tim.color(random_colors())
        tim.circle(100)
        tim.left(angle)
number_of_turns(5)







screen = Screen()
screen.exitonclick()