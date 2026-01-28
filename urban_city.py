from city import *
speed(0)
draw_rekt(-200, -200, 'light blue', 400, 400) #небо
draw_rekt(-200, -200, 'green', 400, 100) #трава
draw_rekt(100, -100, 'light green', 75, 50) #школа
draw_rekt(-170, -150, 'gray', 100, 200) #многоэтажка
draw_rekt(-10, -100, 'white', 100, 75) #магазин
draw_rekt(130, -100, 'brown', 15, 15) #дверь для школы
draw_rekt(110, -75, 'yellow', 10, 10) #окно для школы
draw_rekt(155, -75, 'yellow', 10, 10) #окно для школы
draw_rekt(-155, -110, 'yellow', 30, 30) #окно для многоэтажки
draw_rekt(-155, -55, 'black', 30, 30) #окно для многоэтажки
draw_rekt(-155, -0, 'black', 30, 30) #окно для многоэтажки
draw_rekt(-110, -110, 'black', 30, 30) #окно для многоэтажки
draw_rekt(-110, -55, 'yellow', 30, 30) #окно для многоэтажки
draw_rekt(-110, -0, 'yellow', 30, 30) #окно для многоэтажки
draw_rekt(-10, -45, 'red', 100, 30) #вывеска для магазина
goto(0, -35)
color('white')
write('МАГНИТ', font=('Arial', 15, 'normal'))
draw_rekt(0, -80, 'light blue', 20, 20) #окно для магазина
draw_rekt(60, -80, 'light blue', 20, 20) #окно для магазина
hideturtle()
exitonclick()
