import turtle
from math import sin,cos,radians,degrees,atan2
import random

def android(x0,y0,s,a1,a2,angle,r,g,b) :
    
        turtle.color((r, g, b), (r, g, b))

        angle = -angle
        turtle.goto(x0,y0)
        turtle.setheading(angle)

        rad = radians(angle)

        # 身體正方形
        xp = (-100) * s * cos(rad) - (-100) * s * sin(rad)
        yp = (-100) * s * sin(rad) + (-100) * s * cos(rad)
        turtle.goto(x0+xp,y0+yp)
        turtle.pendown()
        turtle.begin_fill()
        for j in range(1,5,1):
            turtle.forward(200*s)
            turtle.left(90)
        turtle.end_fill()
        turtle.penup()

        #頭
        xp = (100) * s * cos(rad) - (130) * s * sin(rad)
        yp = (100) * s * sin(rad) + (130) * s * cos(rad)
        turtle.goto(x0+xp,y0+yp)
        turtle.left(90)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(100*s, 180)
        turtle.left(90)
        turtle.forward(200*s)
        turtle.end_fill()
        turtle.penup()

        #雙手
        xp = (130) * s * cos(rad) - (90) * s * sin(rad)
        yp = (130) * s * sin(rad) + (90) * s * cos(rad)
        turtle.goto(x0+xp,y0+yp)
        turtle.pensize(35*s)
        turtle.pendown()
        #turtle.setheading(60+angle) ##
        turtle.setheading(a1 + angle)  ##
        turtle.forward(100*s)
        turtle.penup()

        xp = (-130) * s * cos(rad) - (90) * s * sin(rad)
        yp = (-130) * s * sin(rad) + (90) * s * cos(rad)
        turtle.goto(x0+xp,y0+yp)
        turtle.pensize(35*s)
        turtle.pendown()
        #turtle.setheading(240+angle) ##  
        turtle.setheading(a2 + angle)  ##
        turtle.forward(100*s)
        turtle.penup()

        #雙腳
        xp = (60) * s * cos(rad) - (-100) * s * sin(rad)
        yp = (60) * s * sin(rad) + (-100) * s * cos(rad)
        turtle.goto(x0+xp,y0+yp)
        turtle.pensize(35*s)
        turtle.pendown()
        turtle.setheading(310+angle) ##
        turtle.forward(100*s)
        turtle.penup()

        xp = (-60) * s * cos(rad) - (-100) * s * sin(rad)
        yp = (-60) * s * sin(rad) + (-100) * s * cos(rad)
        turtle.goto(x0+xp,y0+yp)
        turtle.pensize(35*s)
        turtle.pendown()
        turtle.setheading(270+angle)  ##
        turtle.forward(100*s)
        turtle.penup()

        #眼睛
        xp = (-30) * s * cos(rad) - (170) * s * sin(rad)
        yp = (-30) * s * sin(rad) + (170) * s * cos(rad)
        turtle.goto(x0+xp,y0+yp)
        turtle.pendown()
        turtle.dot(20*s,'white')
        turtle.penup()

        xp = (30) * s * cos(rad) - (170) * s * sin(rad)
        yp = (30) * s * sin(rad) + (170) * s * cos(rad)
        turtle.goto(x0+xp,y0+yp)
        turtle.pendown()
        turtle.dot(20*s,'white')
        turtle.penup()

        #耳朵
        xp = (35) * s * cos(rad) - (220) * s * sin(rad)
        yp = (35) * s * sin(rad) + (220) * s * cos(rad)
        turtle.goto(x0+xp,y0+yp)
        turtle.pendown()
        turtle.setheading(70+angle) ##
        turtle.pensize(8*s)
        turtle.forward(40*s)
        turtle.penup()

        xp = (-35) * s * cos(rad) - (220) * s * sin(rad)
        yp = (-35) * s * sin(rad) + (220) * s * cos(rad)
        turtle.goto(x0+xp,y0+yp)
        turtle.pendown()
        turtle.setheading(110+angle) ##
        turtle.pensize(8*s)
        turtle.forward(40*s)
        turtle.penup()

turtle.colormode(255)
a=(1200,700)
turtle.setup(a[0],a[1])
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.tracer(0)

list1 = [ x/10 for x in range(-900,600,1) ]
list1 = list1 + list1[::-1]

list2 = [ x/10 for x in range(2400,1200,-1) ]
list2 = list2 + list2[::-1]

i = 0
j = 0

x1 , y1 , s1 = 0 , 0 , 0.2 , # 中心點座標及大小初值設定
x1方向 = 0.2
y1方向 = 0.1
angle1 = int(degrees(atan2(x1方向,y1方向)))
r1 = random.randint(0,255)
g1 = random.randint(0,255)
b1 = random.randint(0,255)

x2 , y2 , s2 = 200 , -200 , 0.2 , # 中心點座標及大小初值設定
x2方向 = -0.1
y2方向 = 0.2
angle2 = int(degrees(atan2(x2方向,y2方向)))
r2 = random.randint(0,255)
g2 = random.randint(0,255)
b2 = random.randint(0,255)

while True :


        android(x1, y1, s1, list1[i],list2[j],angle1,r1,g1,b1)
        android(x2, y2, s2, list1[i],list2[j],angle2,r2,g2,b2)
        turtle.update()
        turtle.clear()
        if i >= len(list1)-1 :
                i = 0
        i += 1
        
        if j >= len(list2)-1 :
                j = 0
        j += 1

        if not -550 <= x1 <= 550:
                x1方向 = -x1方向
                angle1 = int(degrees(atan2(x1方向,y1方向)))
        x1 = x1 + x1方向
        if not -310 <= y1 <= 310:
                y1方向 = -y1方向
                angle1 = int(degrees(atan2(x1方向,y1方向)))            
        y1 = y1 + y1方向
        
        if not -550 <= x2 <= 550:
                x2方向 = -x2方向
                angle2 = int(degrees(atan2(x2方向,y2方向)))
        x2 = x2 + x2方向
        if not -310 <= y2 <= 310:
                y2方向 = -y2方向
                angle2 = int(degrees(atan2(x2方向,y2方向)))            
        y2 = y2 + y2方向