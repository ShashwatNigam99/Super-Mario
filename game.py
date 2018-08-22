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

os.system('clear')
print("\n"*5+" "*45+"SUPER MARIO"+" "*40)
print("\n"*3+" "*30+"Higher the level, more the number of enemies\n")
print(" "*35 + " more gravity and faster movement\n")
print(" "*40 + " Choose Wisely.")
# Initialize the scene
level = int(input(" "*15+"Enter level (1/2/3) : "))

scene = Scene(SC_LENGTH, SC_WIDTH, SC_FULLWIDTH)
# Put mario at predefined initial position
mario = Mario(MARIO_LENGTH, MARIO_WIDTH)
mario.setPos(scene, MARIO_INIT_X, MARIO_INIT_Y)
# scene.start = 150 # remove this after testing
# Generate scene : walls, pits, grass, clouds
generatescene(scene, level)
# Put enemies
putenemies(scene, level, Enemy1.enemies)

getinp = Get()
print(scene.displayScene())

while True:
    input = input_to(getinp, SPEED[level])
    if Lives.lives <= 0:
        print(" You lost all lives. Final score : " +
              str(scene.score))
        sys.exit()
    # change game speed by passing timeout here
    os.system('clear')
    generatescene(scene, level)

    update_enemies(scene, level, Enemy1.enemies)

    print(scene.displayScene())
    if input is not None:
        curhalf = scene.start + SCENE_MOVE_AFTER
        if input in ALLOWED_INPUTS:
            if input == 'd' or input == 'C':
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
                print("lives-1")
                killenemy(scene, mario.y, Enemy1.enemies)
                Lives.lives -= 1

    else:
        mario.gravityfall(scene)
        chk = clashcheck(scene, mario, mario.x, mario.y)
        if chk == 0:
            pass
        elif chk == 2:
            killenemy(scene, mario.y, Enemy1.enemies)
        elif chk == 3:
            print("lives-1")
            killenemy(scene, mario.y, Enemy1.enemies)
            Lives.lives -= 1

    if mario.y > scene.max_y:
        scene.max_y = mario.y
    scene.score = scene.max_y*SCORE_DIST + Enemy1.killed*SCORE_KILLED
