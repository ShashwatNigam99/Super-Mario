from obstacles import *
from config import *


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
    # walls and pits
    Wall.draw_wall(scene, 6, 10, 30)
    Wall.draw_wall(scene, 15, 10, 40)

    wall = Wall(4, 35)
    wall.setPos(scene, groundx-9, 63)

    Pit.draw_pit(scene, 15, 78)

    Wall.draw_wall(scene, 6, 9, 108)
    Pit.draw_pit(scene, 8, 117)
    Wall.draw_wall(scene, 4, 17, 125)
    Pit.draw_pit(scene, 10, 142)

    wall = Wall(3, 10)
    wall.setPos(scene, groundx-12, 170)

    # place enemy on top
    wall = Wall(3, 12)
    wall.setPos(scene, groundx-15, 189)

    Pit.draw_pit(scene, 14, 188)

    wall = Wall(3, 10)
    wall.setPos(scene, groundx-12, 210)

    Pit.draw_pit(scene, 15, 230)

    wall = Wall(3, 3)
    wall.setPos(scene, groundx-7, 233)

    Wall.draw_wall(scene, 6, 10, 245)

    wall = Wall(3, 3)
    wall.setPos(scene, groundx-13, 258)

    Pit.draw_pit(scene, 15, 255)
    Wall.draw_wall(scene, 15, 10, 270)

    wall = Wall(4, 20)
    wall.setPos(scene, groundx-19, 288)
    wall = Wall(3, 22)
    wall.setPos(scene, groundx-27, 300)

    Pit.draw_pit(scene, 50, 280)

    Wall.draw_wall(scene, 15, 10, 330)
    Pit.draw_pit(scene, 15, 340)
    Wall.draw_wall(scene, 6, 10, 355)
    Pit.draw_pit(scene, 15, 365)

    Pit.draw_pit(scene, 100, 390)

    wall = Wall(3, 20)
    wall.setPos(scene, groundx-10, 390)

    wall = Wall(3, 20)
    wall.setPos(scene, groundx-18, 400)

    wall = Wall(3, 20)
    wall.setPos(scene, groundx-27, 410)

    wall = Wall(3, 20)
    wall.setPos(scene, groundx-10, 430)

    wall = Wall(3, 20)
    wall.setPos(scene, groundx-20, 440)

    wall = Wall(3, 10)
    wall.setPos(scene, groundx-25, 467)

    wall = Wall(3, 5)
    wall.setPos(scene, groundx-8, 480)
