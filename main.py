import turtle
from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()
# my_screen = Screen()
#
# print(timmy)
# print(my_screen.canvheight)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# my_screen.exitonclick()

table = PrettyTable()
table.add_column("pokemon name",["Pikachu", "Squirtle", "Salamander"])
table.add_column("pokemon Type", ["Electric", "Water", "Fire"])
table.align = 'l'
print(table)