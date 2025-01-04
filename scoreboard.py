from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        #self.goto(-40,270)
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_score()

    def l_point(self):
        self.l_score +=1
        print("left score",self.l_score)
        self.clear()
        self.update_score()

    def r_point(self):
        self.r_score +=1
        print("right score",self.r_score)
        self.clear()
        self.update_score()

    def update_score(self):
        self.goto(-200, 200)
        self.color("red")
        self.write(f" Score {self.l_score}", align='left', font=('Courier', 20, 'normal'))
        self.goto(100, 200)
        self.write(f" Score {self.r_score}", align='left', font=('Courier', 20, 'normal'))
