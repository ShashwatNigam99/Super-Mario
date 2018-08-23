import os
import sys
import time
from config import *
from scene import Scene
from people import *
from obstacles import *
from scene_gen import *
from input import *
from gamefunctions import *

level = show_title_page()
# Initialize the scene
scene = Scene(SC_LENGTH, SC_WIDTH, SC_FULLWIDTH)
# Put mario at predefined initial position
mario = Mario(MARIO_LENGTH, MARIO_WIDTH)
mario.setPos(scene, MARIO_INIT_X, MARIO_INIT_Y)
# Generate scene : walls, pits, grass, clouds
generatescene(scene, level)
# Put enemies
putenemies(scene, level, Enemy1.enemies)
putcoins(scene, level, Coins.coins)

getinp = Get()
print(scene.displayScene(level))

while True:
    input = input_to(getinp, SPEED[level])
    # check if the player hasn't lost all lives
    check_lives(scene, Lives.lives)
    os.system('clear')
    generatescene(scene, level)
    # update all alive enemies
    update_enemies(scene, level, Enemy1.enemies)
    update_coins(scene, level, Coins.coins)
    # display the scene generated
    print(scene.displayScene(level))
    if input is not None:
        curhalf = scene.start + SCENE_MOVE_AFTER
        if input in ALLOWED_INPUTS:
            if input in ['d', 'C']:
                if(mario.y <= curhalf):
                    mario.move(input, scene)
                else:
                    scene.start += mario.step
                    mario.move(input, scene)
            else:
                mario.move(input, scene)

        if input == 'q':
            os.system('clear')
            sys.exit()
        else:
            mario.gravityfall(scene)
            chk = clashcheck(scene, mario, mario.x, mario.y)
            if chk == 0:
                pass
            elif chk == 2:
                killenemy(scene, mario.y, Enemy1.enemies)
            elif chk == 3:
                killenemy(scene, mario.y, Enemy1.enemies)
                Lives.lives -= 1
            elif chk == 4:
                collect_coin(scene, mario.y, Coins.coins)

    else:
        mario.gravityfall(scene)
        chk = clashcheck(scene, mario, mario.x, mario.y)
        if chk == 0:
            pass
        elif chk == 2:
            killenemy(scene, mario.y, Enemy1.enemies)
        elif chk == 3:
            killenemy(scene, mario.y, Enemy1.enemies)
            Lives.lives -= 1
        elif chk == 4:
            collect_coin(scene, mario.y, Coins.coins)

    if mario.y > scene.max_y:
        scene.max_y = mario.y
    scene.score = scene.max_y*SCORE_DIST + Enemy1.killed * \
        SCORE_KILLED + Coins.collected*SCORE_COINS
