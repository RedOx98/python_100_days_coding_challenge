import colorgram
from turtle import Turtle, Screen
import random

# C:\Users\HROlaide\Downloads\download.jpg
# Extract 6 colors from an image.

# rgb_colors=[]
# colors = colorgram.extract("C:\\Users\\HROlaide\\Downloads\\download.jpg", 6)
# first_color=colors[0]
# # print(first_color.rgb)
# for color in colors:
#
#     r= color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r,g,b)
#     rgb_colors.append(new_colors)
# print(rgb_colors)

color_list = [(248, 247, 240), (239, 250, 245), (251, 241, 247), (237, 243, 250), (235, 226, 87), (210, 161, 109)]

# Setup turtle and screen
screen = Screen()
screen.colormode(255)   # Enable RGB color mode
timmy = Turtle()
timmy.hideturtle()
timmy.speed("fastest")
timmy.penup()

# Starting position (bottom-left)
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

# Draw 10x10 grid of spots
for row in range(10):
    for col in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)

screen.exitonclick()
