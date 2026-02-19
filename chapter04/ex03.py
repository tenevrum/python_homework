import turtle
import math

bob = turtle.Turtle()

def triangle_pie(t: turtle.Turtle, n: float, radius: float):
    '''Рисует плотно прилегающие треугольники друг к другу,
    которые замыкаются и таким образом получается многоугольник'''
    apex_angle = 360/n
    base_angle = (180 - apex_angle)/2
    base = 2*radius*math.sin(math.radians(apex_angle/2))
    for i in range(n):
        t.forward(radius)
        t.left(180 - base_angle)
        t.forward(base)
        t.left(180 - base_angle)
        t.forward(radius)
        t.left(180)
        
def move(t):
    '''Двигает черепашку вправо'''
    t.penup()
    t.forward(250)
    t.pendown()
    
triangle_pie(bob, 5, 100)
move(bob)
triangle_pie(bob, 6, 100)
move(bob)
triangle_pie(bob, 7, 100)

turtle.done()
