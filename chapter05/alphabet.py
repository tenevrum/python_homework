import turtle
import math

bob = turtle.Turtle()
hight = 50

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

def diagonal(t: turtle.Turtle):
   cathetus1 = hight
   cathetus2 = hight*2/3
   hypotenuse = math.sqrt((cathetus1)**2 + (cathetus2)**2)
   smaller_angle = math.degrees(math.atan(cathetus2/cathetus1))
   angle = 90 - smaller_angle
   t.left(angle)
   t.forward(hypotenuse)
   t.right(180-smaller_angle)

def narrow_diagonal(t: turtle.Turtle):
   cathetus1 = hight
   cathetus2 = hight/3
   hypotenuse = math.sqrt((cathetus1)**2 + (cathetus2)**2)
   smaller_angle = math.degrees(math.atan(cathetus2/cathetus1))
   angle = 90 - smaller_angle
   t.left(angle)
   t.forward(hypotenuse)

def small_diagonal(t: turtle.Turtle):
   cathetus1 = hight*2/3
   cathetus2 = cathetus1*1.5/2
   hypotenuse = math.sqrt(cathetus1**2 + (cathetus2)**2)
   smaller_angle = math.degrees(math.atan(cathetus2/cathetus1))
   angle = 90 - smaller_angle
   t.left(angle)
   t.forward(hypotenuse)
   t.right(180-smaller_angle)

def small_diagonal_left(t: turtle.Turtle):
   cathetus1 = hight*2/3
   cathetus2 = cathetus1*1.5/2
   hypotenuse = math.sqrt(cathetus1**2 + (cathetus2)**2)
   smaller_angle = math.degrees(math.atan(cathetus2/cathetus1))
   angle = 90 - smaller_angle
   t.left(smaller_angle)
   t.forward(hypotenuse)
   t.right(180-angle)

def smaller_diagonal(t: turtle.Turtle):
   cathetus1 = hight/2
   cathetus2 = cathetus1*1/1.5
   hypotenuse = math.sqrt(cathetus1**2 + (cathetus2)**2)
   smaller_angle = math.degrees(math.atan(cathetus2/cathetus1))
   angle = 90 - smaller_angle
   t.left(angle)
   t.forward(hypotenuse)

def print_a(t: turtle.Turtle):
    diagonal(bob)
    t.forward(hight)
    t.right(180)
    t.penup()
    t.forward(hight/2)
    t.pendown()
    t.left(90)
    t.forward(hight/3)
    t.penup()
    t.left(90)
    t.forward(hight/2)
    t.left(90)
    t.forward(hight*2/3)
    t.pendown()

def print_b(t: turtle.Turtle):
    t.left(90)
    t.forward(hight)
    t.right(90)
    for i in range(2):
        t.forward(hight*2/3-hight/4)
        arc(t, hight/4, -180)
        t.forward(hight*2/3-hight/4)
        t.left(180)
    t.penup()
    t.forward(hight)
    t.pendown()

def letter_c(t: turtle.Turtle):
    t.penup()
    t.forward(hight*2/3)
    t.left(90)
    t.forward(hight/3)
    t.pendown()
    t.left(180)
    arc(t, hight/3, -180)
    t.forward(hight/3)
    arc(t, hight/3, -180)
    
def move_c(t: turtle.Turtle):
    t.penup()
    t.forward(hight*2/3)
    t.left(90)
    t.forward(hight/3)
    t.pendown()

def print_c(t: turtle.Turtle):
    letter_c(bob)
    move_c(bob)

def print_d(t: turtle.Turtle):
    t.forward(hight*2/3-hight/2)
    arc(t, hight/2, 180)
    t.forward(hight*2/3-hight/2)
    t.left(90)
    t.forward(hight)
    t.left(90)
    t.penup()
    t.forward(hight)
    t.pendown()

def print_e(t: turtle.Turtle):
    t.forward(hight*2/3)
    t.back(hight*2/3)
    print_f(bob)

def print_f(t: turtle.Turtle):
    t.left(90)
    t.forward(hight)
    t.right(90)
    t.forward(hight*2/3)
    t.back(hight*2/3)
    t.right(90)
    t.forward(hight/2)
    t.left(90)
    t.forward(hight/3)
    t.back(hight/3)
    t.penup()
    t.right(90)
    t.forward(hight/2)
    t.left(90)
    t.forward(hight)
    t.pendown()

def print_g(t: turtle.Turtle):
    letter_c(bob)
    t.penup()
    t.forward(hight/3)
    t.right(90)
    t.pendown()
    t.forward(hight/3)
    t.penup()
    t.left(90)
    t.forward(hight/3)
    t.left(90)
    t.forward(hight*2/3)
    t.pendown()

def print_h(t: turtle.Turtle):
    t.left(90)
    t.forward(hight)
    t.back(hight/2)
    t.right(90)
    t.forward(hight*2/3)
    t.left(90)
    t.forward(hight/2)
    t.back(hight)
    t.right(90)
    t.penup()
    t.forward(hight/3)
    t.pendown()

def letter_t(t: turtle.Turtle):
    t.penup()
    t.left(90)
    t.forward(hight)
    t.right(90)
    t.pendown()
    t.forward(hight*2/3)
    t.back(hight/3)
    t.right(90)
    t.forward(hight)

def move_t(t: turtle.Turtle):
    t.penup()
    t.left(90)
    t.forward(hight*2/3)
    t.pendown()

def print_i(t: turtle.Turtle):
    letter_t(bob)
    t.right(90)
    t.forward(hight/3)
    t.back(hight*2/3)
    t.left(180)
    t.penup()
    t.forward(hight/3)
    t.pendown()

def print_j(t: turtle.Turtle):
    t.penup()
    t.left(90)
    t.forward(hight)
    t.pendown()
    for i in range(2):
        t.right(90)
        t.forward(hight*2/3)
    arc(t, hight/3, -180)
    t.penup()
    t.right(90)
    t.forward(hight)
    t.right(90)
    t.forward(hight/3)
    t.left(90)
    t.pendown()

def print_k(t: turtle.Turtle):
    t.left(90)
    t.forward(hight)
    t.back(hight/2)
    t.right(180)
    small_diagonal(bob)
    t.penup()
    t.forward(hight*2/3)
    t.right(90)
    t.forward(hight/2)
    t.right(90)
    t.pendown()
    small_diagonal_left(bob)
    t.penup()
    t.forward(hight)
    t.left(90)
    t.forward(hight/3)
    t.pendown()

def print_l(t: turtle.Turtle):
    t.left(90)
    t.forward(hight)
    t.back(hight)
    t.right(90)
    t.forward(hight*2/3)
    t.penup()
    t.forward(hight/3)
    t.pendown()

bob.teleport(-700, 0)
print_a(bob)
print_a(bob)
print_b(bob)
print_c(bob)
print_d(bob)
print_e(bob)
print_f(bob)
print_g(bob)
print_h(bob)
print_i(bob)
print_j(bob)
print_k(bob)
print_l(bob)

turtle.done()
