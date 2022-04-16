from turtle import Turtle, Screen
screen = Screen()

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN =270
LEFT = 180
RIGHT = 0


class Snake():

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_snake(position)

    def add_snake(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snakes.append(snake)

    def reset(self):
        for seg in self.snakes:
            seg.goto(1000, 1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]

    def extend(self):
        self.add_snake(self.snakes[-1].position())

    def move(self):
        for s in range(len(self.snakes)-1, 0, -1):
            nex_x = self.snakes[s - 1].xcor()
            nex_y = self.snakes[s - 1].ycor()
            self.snakes[s].goto(nex_x, nex_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
