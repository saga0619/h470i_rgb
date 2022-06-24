import h470i_rgb
import time
from random import randint


controller = h470i_rgb.AorusRGBController()
while True:
    time.sleep(1)
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    controller.set_rgb("IO_LED",r,g,b)

