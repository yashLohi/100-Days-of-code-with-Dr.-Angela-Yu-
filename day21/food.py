from turtle import Turtle
import random


# The food is also a turtle so we inherit the turtle class
class Food(Turtle):

    def __init__(self):
        super().__init__()  # this is how we inherit the class
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()


    # Refresh function works when ever the snake eat he present food
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
