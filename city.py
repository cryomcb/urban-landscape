from turtle import *
def draw_rekt(x, y, color_r, w, h):
    penup()
    goto(x, y)
    pendown()
    color(color_r)
    begin_fill()
    for i in range(2):
        forward(w)
        left(90)
        forward(h)
        left(90)
    end_fill()
