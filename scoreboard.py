from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.write(f"{self.score1} : {self.score2}", align=ALIGNMENT, font=FONT)

    def add_point1(self):
        self.clear()
        self.score1 += 1
        self.write(f"{self.score1} : {self.score2}", align=ALIGNMENT, font=FONT)

    def add_point2(self):
        self.clear()
        self.score2 += 1
        self.write(f"{self.score1} : {self.score2}", align=ALIGNMENT, font=FONT)

    def user1_win(self):
        self.goto(0, 50)
        self.write("User 1 Wins!", align=ALIGNMENT, font=FONT)

    def user2_win(self):
        self.goto(0, 50)
        self.write("User 2 Wins!", align=ALIGNMENT, font=FONT)
