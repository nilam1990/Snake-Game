from turtle import Turtle
SEGMENT_POSITION = [(0, 0), (-20, 0), (-40, 0)]
SEGMENT_MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        """ initialize snake body"""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """ create snake body """
        for position in SEGMENT_POSITION:
            self.add_segments(position)

    def add_segments(self, position):
        """ add segment to snake """
        tur = Turtle("square")
        tur.color("white")
        tur.penup()
        tur.goto(position)
        self.segments.append(tur)

    def extend_snake(self):
        """ extend snake from last segment"""
        self.add_segments(self.segments[-1].position())

    def snake_move(self):
        """ Move a snake 20 px forword"""
        for seg_no in range(len(self.segments) - 1, 0, -1):
            new_x_cor = self.segments[seg_no - 1].xcor()
            new_y_cor = self.segments[seg_no - 1].ycor()
            self.segments[seg_no].goto(new_x_cor, new_y_cor)
        self.segments[0].forward(SEGMENT_MOVE)

    def up(self):
        """ turn a snake up """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """ turn a snake down """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """ turn a snake to left """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """ turn a  snake to right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
