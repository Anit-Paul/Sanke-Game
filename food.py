from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed('fastest')
        
    def give_food(self,snake):
        positions=set()
        for i in snake.body:
            positions.add(i.pos())
        x=-290
        y=-290
        while (x,y) in positions or x==-290 or x==290 or y==-290 or y==290:
            x=random.randint(-290,290)
            y=random.randint(-290,290)
        self.goto(x=x,y=y)
            
        
        
        