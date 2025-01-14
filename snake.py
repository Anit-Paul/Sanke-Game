from turtle import Turtle

class Snake:
    def __init__(self):
        self.n=3
        self.body=[]
        self.__create_snake()
        self.head=self.body[0]
    def increase(self):
        self.body.append(Turtle())
        self.body[-1].penup()
        self.body[-1].shape('square')
        self.body[-1].color('white')
        self.body[-1].goto(self.body[-2].pos())
    def __create_snake(self):
        w=20
        for i in range(self.n):
            self.body.append(Turtle())
            self.body[-1].penup()
            self.body[-1].shape('square')
            self.body[-1].color('white')
            self.body[-1].goto(x=w-20,y=0)
            w-=20 
            
    def move(self):
        for i in range(len(self.body)-1,0,-1):
            x,y=self.body[i-1].pos()
            self.body[i].goto(x,y)
        self.body[0].fd(20)
    
    def dead(self):
        x, y = self.head.pos()
        if x >= 290 or x <= -290 or y >= 290 or y <= -290:
            return False 

        for i in range(1, len(self.body)):
            if self.head.distance(self.body[i]) < 10:
                return False 

        return True

    
    def up(self,direction):
        if direction=='down':
            return False
        self.body[0].setheading(90)
        return True
    def down(self,direction):
        if direction=='up':
            return False
        self.body[0].setheading(270)
        return True
    def left(self,direction):
        if direction=='right':
            return False
        self.body[0].setheading(180)
        return True
    def right(self,direction):
        if direction=='left':
            return False
        self.body[0].setheading(360)
        return True
        