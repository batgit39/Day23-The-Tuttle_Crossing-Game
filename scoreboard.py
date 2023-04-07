from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.score += 1
        self.goto(-200,260)
        self.write(f"Level: {self.score}", align = "center", font = ("Courier", 24 , "normal"))


