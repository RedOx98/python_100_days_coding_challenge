import random
from turtle import Turtle, Screen

timmy= Turtle()
timmy.shape("arrow")
timmy.color("red")

# dashed lines
# for _ in range(10):
#     timmy.forward(10)  # draw a dash
#     timmy.penup()  # lift the pen (no drawing)
#     timmy.forward(10)  # move forward to create a gap
#     timmy.pendown()
    # timmy.left(90)
    # timmy.forward(20)
    # timmy.left(90)
    # timmy.forward(20)
    # timmy.left(90)
    # timmy.forward(20)

#     Overlapping hsapes from triangle to nonagon
colors = ["red", "orange", "yellow", "green", "blue", "purple", "brown", "pink", "cyan"]

# Draw polygons from 3 sides (triangle) up to 9 sides (nonagon)
# for sides in range(3, 11):
#     angle = 360 / sides
#     timmy.color(colors[sides - 3])  # pick a color for each shape
#     for _ in range(sides):
#         timmy.forward(100)
#         timmy.right(angle)

timmy.speed("fastest")

# Set up screen and color mode
Screen().colormode(255)

def random_color():
    """Generate a random RGB color"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
#
# # Possible directions (in degrees)
# directions = [0, 90, 180, 270]
#
# # Start random walk
# for _ in range(200):
#     timmy.color(random_color())
#     timmy.pensize(random.randint(2, 10))  # make line thickness random
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

def draw_spirograph(size_of_gap):
    """Draw a spirograph with a given rotation gap in degrees"""
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograph(10)


Screen()
Screen().exitonclick()