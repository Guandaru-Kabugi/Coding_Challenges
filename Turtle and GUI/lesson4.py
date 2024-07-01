from turtle import Turtle,Screen
import random
tim = Turtle()
tim.shape("turtle")
tim.color("blue")
tim.pensize(10)

colors = ("orange red","medium slate blue","violet","orange","green","blue", "sea green")
counting = 0
while counting <50:
    tim.pencolor(random.choice(colors))
    counting+=1
    if (-300 < tim.xcor() <300) and (-300 < tim.ycor() <300):
        tim.right(random.randint(0,360))
        distance = random.randint(30,100) 
        tim.forward(distance)
    else:
        tim.right(180)
        tim.forward(distance)
    









screen = Screen()
screen.exitonclick()