from turtle import Turtle
from random import randint
START_ANGLES = randint(150, 210)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setheading(START_ANGLES)
        self.speed("fastest")

    def bounce_vertical(self):
        self.setheading(180 - self.heading())

    def bounce_horizontal(self):
        self.setheading(0 - self.heading())

    def refresh(self):
        self.setposition(0, 0)
        self.setheading(START_ANGLES)
