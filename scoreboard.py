from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Ariel", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        """ update score"""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """ display game over in middle of screen"""
        self.goto(0, 0)
        self.write(f"GAME OVER ", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """ increase score if snake eats food """
        self.score += 1
        self.clear()
        self.update_score()
