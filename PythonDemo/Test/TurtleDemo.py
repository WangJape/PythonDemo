from turtle import *

color("blue", "red")
begin_fill()
while True:
    forward(200)
    right(144)
    if abs(pos()) < 1:
        break
end_fill()
