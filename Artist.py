import turtle
import math


class Artist:
    def __init__(self, t):
        self.t = t

    def move(self,x,y):
        self.t.penup()
        self.t.goto(x,y)
        self.t.pendown()

    def triangle(self,size = 100):
        for i in range(3):
            self.t.right(120)
            self.t.forward(size)
            
    def square(self,size = 100):
        for i in range(4):
            self.t.right(90)
            self.t.forward(size)
            
    def drawcircle(self, size = 100):
       for i in range (360):
           self.t.left(1)
           self.t.forward(size/100)
           
    def star(self,size = 100):
        for i in range (5):
            self.t.forward(size)
            self.t.right(144)
            
    def polygon(self, n=5, size = 100):
        for i in range (n):
            self.t.forward(size)
            self.t.right(180-(n-2)*180/n)
            
    def rhombus(self,angle = 30,size=100):
            self.t.right((180-angle)/2)
            self.t.forward(size)
            self.t.right(180-angle)
            self.t.forward(size)
            self.t.right(angle)
            self.t.forward(size)
            self.t.right(180-angle)
            self.t.forward(size)

    def mountain(self, size = 100):
            self.t.left(75)
            self.t.forward(size)
            self.t.right(105)
            self.t.forward(size*0.5)
            self.t.left(105)
            self.t.forward(size)
            self.t.right(150)
            self.t.forward(size)
            self.t.left(105)
            self.t.forward(size*0.5)
            self.t.right(105)
            self.t.forward(size)
            self.t.right(75)
            self.t.goto(150,-150)
           
        

     


def main():
    canvas = turtle.Screen()
    canvas.bgcolor("cyan")
    canvas.title("Turtle Example")
    
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(5)
    
    a = Artist(t)
    a.move(-250,150)
    a.drawcircle(100)
    
    a.move(-100,150)
    a.square()
    
    a.move(0,150)
    a.triangle(50)
    
    a.move(50,150)
    a.star()
    
    a.move(0,-50)
    a.polygon(6,50)

    a.move(150,-150)
    a.mountain()

    a.move(-250,-50)
    a.rhombus(30,80)

    
    





if __name__ == "__main__":
    main()
