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
    for y in range(55, 500, 45):
        grass = Grass(2, 3)
        x = groundx - grass.length
        grass.setPos(scene, x, y)
    # walls
    Wall.draw_wall(scene, 6, 5, 40)
    Wall.draw_wall(scene, 15, 5, 45)

    wall = Wall(5, 35)
    wall.setPos(scene, groundx-12, 63)

    Pit.draw_pit(scene, 15, 78)

    Wall.draw_wall(scene, 15, 5, 108)
    Wall.draw_wall(scene, 6, 5, 113)
