from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()

    def create_paddle(self, x_cor):
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(x_cor, 0)

    def up(self):
        self.setposition(x=-350, y=self.ycor() + 25)

    def down(self):
        self.setposition(x=-350, y=self.ycor() - 25)

    def up2(self):
        self.setposition(x=350, y=self.ycor() + 25)

    def down2(self):
        self.setposition(x=350, y=self.ycor() - 25)
