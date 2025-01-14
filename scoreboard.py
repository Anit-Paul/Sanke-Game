from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.update_score()
        self.hideturtle()
    
    def update_score(self):
        self.clear()
        self.write(f'Score : {self.score}', move=False, align='center', font=('Arial', 15, 'normal'))
    
    def over(self):
        self.goto(0,0)
        self.write(f'Game Over!', move=False, align='center', font=('Arial', 15, 'normal'))
    
        