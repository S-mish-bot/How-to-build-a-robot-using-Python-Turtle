# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 05:04:34 2020

@author: Dell
"""

import turtle as t
t.bgcolor("Black")
def rectangle(h,v,c):
    t.shape("turtle")
    t.setheading(0)
    
    t.pendown()
    t.speed("slowest")
    
    t.pensize(2)
    t.begin_fill()
    for i in range(2):
        t.color(c)
        t.forward(h)
        t.left(90)
        t.forward(v)
        t.left(90)
    t.end_fill()
    t.penup()
#feet
t.goto(-100,-150)
rectangle(50,20,"red")
t.goto(-20,-150)
rectangle(50,20,"red")
#legs
t.goto(-80,-130)
rectangle(20,60,"Yellow")
t.goto(-10,-130)
rectangle(20,60,"Yellow")

#body
t.goto(-90,-70)
rectangle(110,160,"Blue")

#hands
t.goto(20,10)
rectangle(50,15,"Yellow")

t.goto(-140,10)
rectangle(50,15,"Yellow")

t.goto(55,10)
rectangle(15,50,"Yellow")

t.goto(-140,10)
rectangle(15,50,"Yellow")
#neck
t.goto(-43,92)
rectangle(17,22,"Yellow")

#head
t.goto(-70,105)
rectangle(70,50,"Blue")

#eyes
t.goto(-55,140)
rectangle(44,7,"White")

#eyeballs

t.goto(-48,141)
rectangle(9,7,"Black")

t.goto(-20,141)
rectangle(9,7,"Black")

t.goto(-58,120)
rectangle(50,4,"White")

t.goto(0,0)

