from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.i = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.write(arg=f"Score: {self.i} High Score: {self.high_score}", move=False, align="center", font=("Courier", 20, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.i += 1
        self.clear()
        self.write(arg=f"Score: {self.i} High Score: {self.high_score}", move=False, align="center", font=("Courier", 24, "normal"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="Game over!", move=False, align="center", font=("Courier", 24, "normal"))

    def reset(self):
        if self.i > self.high_score:
            self.high_score = self.i
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.i = 0
        self.increase_score()



