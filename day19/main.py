import random
import turtle
from turtle import Screen

tim = turtle.Turtle()
screen = Screen()
screen.setup(500, 300)
# def move_forwards():
#     tim.forward(10)
#
# screen.listen()
# screen.onkey(key="space", fun=move_forwards)
# screen.exitonclick()

# Etch a sketch game
# tim.shape("turtle")
# tim.color("blue")
# tim.speed("fastest")
#
# # Define movement functions
# def move_forward():
#     tim.forward(20)
#
# def move_backward():
#     tim.backward(20)
#
# def turn_left():
#     tim.left(15)
#
# def turn_right():
#     tim.right(15)
#
# def clear_drawing():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# # Set up the screen and key bindings
# screen = Screen()
# screen.listen()
#
# screen.onkey(move_forward, "w")
# screen.onkey(move_backward, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear_drawing, "c")


screen.setup(width=800, height=400)
screen.title("🏁 Turtle Race Game 🐢")
# screen.bgcolor("black")

# Rainbow colors
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Ask the user to guess the winning color
user_bet = screen.textinput(title="Make your bet 🎨",
                            prompt="Which turtle will win the race? Enter a color: ").lower()

# Create turtles
all_turtles = []
start_y = -120

for color in colors:
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-350, y=start_y)
    start_y += 40
    all_turtles.append(new_turtle)

# Start race
race_on = False
if user_bet:
    race_on = True

while race_on:
    for racer in all_turtles:
        # Move each turtle a random distance
        distance = random.randint(0, 10)
        racer.forward(distance)

        # Check if any turtle has crossed the finish line
        if racer.xcor() > 350:
            race_on = False
            winning_color = racer.pencolor()
            if winning_color == user_bet:
                print(f"🎉 You’ve won! The {winning_color} turtle is the winner!")
            else:
                print(f"😞 You’ve lost! The {winning_color} turtle won the race.")
            break
screen.exitonclick()