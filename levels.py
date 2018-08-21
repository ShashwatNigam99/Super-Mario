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
    # walls and pits
    Wall.draw_wall(scene, 6, 10, 30)
    Wall.draw_wall(scene, 15, 10, 40)

    wall = Wall(5, 35)
    wall.setPos(scene, groundx-12, 63)

    Pit.draw_pit(scene, 15, 78)

    Wall.draw_wall(scene, 13, 9, 108)
    Pit.draw_pit(scene, 15, 117)
    Wall.draw_wall(scene, 6, 10, 132)
    Pit.draw_pit(scene, 15, 142)


# used to initially put all enemies at their initial positons
#def putenemies(scene, level):
#    bot = Enemy1(4, 6, 160, 250)
#    enemies.append(bot)
#    bot.setPos(scene, groundx-bot.length, bot.lpos)


#def update_enemies(scene, level):
#    for bot in enemies:
#        print("update")
#        if bot.direction == 1:
#            bot.setPos(scene, bot.x, bot.y + bot.step)
#        elif bot.direction == -1:
#            bot.setPos(scene, bot.x, bot.y - bot.step)
#        if(bot.y >= bot.rpos or bot.y <= bot.lpos):
#            bot.direction *= -1
#        print(bot.x, bot.y)
