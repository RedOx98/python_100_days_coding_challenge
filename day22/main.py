from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scores import Scoreboard
import time

# Setup screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("🏓 Pong Game")
screen.tracer(0)

# Middle dashed line
divider = Turtle()
divider.color("white")
divider.penup()
divider.hideturtle()
divider.goto(0, 300)
divider.setheading(270)
for _ in range(30):
    divider.pendown()
    divider.forward(10)
    divider.penup()
    divider.forward(10)

# Create paddles, ball, and scoreboard
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Control paddles
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
#
#     # Bounce on top or bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
#
    # Bounce on paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or \
       (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
#
#     # Right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    # --- WIN CONDITION ---
    if scoreboard.l_score >= 10:
        game_is_on = False
        scoreboard.game_over("🏆 Player 1 (Left) Wins!")
    elif scoreboard.r_score >= 10:
        game_is_on = False
        scoreboard.game_over("🏆 Player 2 (Right) Wins!")

screen.exitonclick()