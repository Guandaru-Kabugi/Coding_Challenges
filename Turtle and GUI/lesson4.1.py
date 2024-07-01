from turtle import Turtle,Screen
import random
tim = Turtle()
tim.shape("turtle")
tim.color("blue")
tim.pensize(10)
tim.speed("fastest")

colors = ("orange red","medium slate blue","violet","orange","green","blue", "sea green")
counting = 0
directions = [0,90,180,270]

for _ in range (200):
    tim.pencolor(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))








screen = Screen()
screen.exitonclick()