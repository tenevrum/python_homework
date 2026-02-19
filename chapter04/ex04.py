import turtle
import math

bob = turtle.Turtle()
bob.speed(0)

def polyline(t: turtle.Turtle, n: int, length: float, angle: float):
    for i in range(n):
        t.forward(length)
        t.left(angle)

def arc(t: turtle.Turtle, radius: float, angle: float):
    arc_length = 2 * math.pi * radius * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = angle / n
    t.left(step_angle / 2)
    polyline(t, n, step_length, step_angle)
    t.right(step_angle / 2)

def petal(t: turtle.Turtle, radius: float, angle: float):
    '''Рисует один лепесток из двух дуг'''
    arc(t, radius, angle)
    t.left(180 - angle)
    arc(t, radius, angle)
    t.left(180 - angle)

def flower(t: turtle.Turtle, n: int, radius: float):
    '''Рисует цветок из n лепестков'''
    angle = 360/n
    for i in range(n):
        petal(t, radius, angle)
        t.left(angle)

def move(t: turtle.Turtle):
    '''Двигает черепашку вправо'''
    t.penup()
    t.forward(150)
    t.pendown()

# Цветок слева
flower(bob, 7, 80)
move(bob)

# Цветок посередине
flower(bob, 5, 60)
bob.left(180)
flower(bob, 5, 60)
bob.left(180)
move(bob)

# Последний цветок
flower(bob, 20, 200)

turtle.done()
