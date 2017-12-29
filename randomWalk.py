from microbit import *
import random

i=2;
j=2;

def blink(i,j,dur=100):
    display.set_pixel(i, j, 9)
    sleep(dur)
    display.set_pixel(i, j, 0)

while True:
    blink(i,j)
    dir=random.randint(-1,2)
    if dir%2==0:
        j=max(min(j+dir-1,4),0)
    else:
        i=max(min(i+dir,4),0)
