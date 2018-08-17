import random
from obstacles import *
from scene import *


def generatescene(scene, level):

    # clouds
    x = 0
    for y in range(10, 500, 30):
        cloud = Cloud(3, 6)
        x = (x+2) % 7
        cloud.setPos(scene, x, y)
    # grass
    for y in range(50, 500, 45):
        grass = Grass(2, 3)
        x = groundx - grass.length
        grass.setPos(scene, x, y)
