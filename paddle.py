from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,new_xcor,new_ycor):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1, outline=None)
        self.penup()
        self.goto(new_xcor, new_ycor)

    def up(self):
        print("up function")
        new_y = self.ycor() + 20
        # paddle.penup()
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        # paddle.penup()
        self.goto(self.xcor(), new_y)
