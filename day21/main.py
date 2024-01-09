from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Create a screen of width 600 X 600 with black color and 0 delay title the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Snake class
snake = Snake()
# Food Class
food = Food()
# Scoreboard Class
scoreboard = Scoreboard()

# This is for button which snake follow
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Start the game
game_is_on = True
while game_is_on:
    # to handle the snake delay
    screen.update()
    # update in 0.1 secs
    time.sleep(0.1)
    # Move class which contiune move the snake forward
    snake.move()

    # Detect collision with food.
    # if the snake head distance from food is less than 15 that means snake eat a food
    if snake.head.distance(food) < 15:
        # change the food position
        food.refresh()
        # increase the snake length
        snake.extend()
        # increase score
        scoreboard.increase_score()

    # Detect collision with wall.

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        # called the game over function
        scoreboard.game_over()

    # Detect collision with tail.
    # for checking the collision of sanke with his own body we check head distance from its
    # other segment
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
