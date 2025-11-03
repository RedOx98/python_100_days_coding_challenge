from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("🐢 Turtle Crossing Game")

game_on = True

player = Player()
score = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")

while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_on = False

    # Detect successful crossing
    if player.is_at_finish_line():
        player.goto_start()
        car_manager.level_up()
        score.increase_level()




screen.exitonclick()