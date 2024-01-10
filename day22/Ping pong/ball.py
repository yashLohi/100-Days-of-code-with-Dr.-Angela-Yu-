from turtle import Turtle

# ball has a functionality to move to the new position
#

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):   # when ball touch the upper and lower wall
        self.y_move *= -1

    def bounce_x(self):   # when ball touch the paddles the increase the slight in speed
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):  # when ball miss the paddle they go the original position
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
