from turtle import*
from colorsys import*
bgcolor("black")
title("study much")
width(2)
speed(0)
n=160
for i in range(n):
    c = hsv_to_rgb(i/6,i/n,1)
    fillcolor(c)
    begin_fill()
    (80)
    circle(i*1.2,80)
    end_fill()
    rt(59)
ht()
done



