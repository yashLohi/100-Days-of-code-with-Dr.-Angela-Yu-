from turtle import Turtle

# for creating the snake we need three turtle below are their starting position
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    # initalizing the snake we create a list called segments
    # then it called the create_snake class
    # we assign the head of sanke to segments[0]
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # for creating are starting snake we pass the position where we want are snake
    # the function internally called the add segment function with position parameter
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # For creating snake we had to create a 3 turtle so we define their position where are they going to
    # align at their starting position
    # we create a list called segments whenever we create a snake we append it in the list
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    # when snake eat food we extend the snake length by adding the a new turtle in last position
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # for moving the snake we applied the logic to overlap the turtles
    # like we first have three turtle to move we first : put the third turtle on the position of the second position
    # and second on the place of first and first on the new position
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
