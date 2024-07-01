from turtle import Turtle,Screen
import random
tim = Turtle()
tim.shape("turtle")
tim.color("blue")

def draw_shapes (no_sides):
    
    angle = 360/no_sides
    for _ in range (no_sides):
        
        tim.forward(100)
        tim.right(angle)
for number in range (3,11):
    colors = ("orange red","medium slate blue","violet","orange","green","blue", "sea green")
    tim.pencolor(random.choice(colors))
    draw_shapes(number)
    
    
    









screen = Screen()
screen.exitonclick()