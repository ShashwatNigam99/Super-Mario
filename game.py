import os
import sys
import time
from scene import Scene
from people import *
from obstacles import *
from levels import *
from input import *
from gamefunctions import *

# Initialize the scene
scene = Scene(40, 100, 500)
# Put mario at predefined initial position
mario = Mario(4, 3)
mario.setPos(scene, 32, 4)
# Generate scene : walls, pits, grass, clouds
generatescene(scene, 1)
# Put enemies
putenemies(scene, 1, Enemy1.enemies)

getinp = Get()
print(scene.displayScene())

while True:
    input = input_to(getinp)
    os.system('clear')
    generatescene(scene, 1)

    update_enemies(scene, 1, Enemy1.enemies)

    print(scene.displayScene())
    if input is not None:
        curhalf = scene.start + 60
        if input in ['w', 'a', 'd']:
            if input == 'd':
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
            print("kill called from game")
            killenemy(scene, mario.y, Enemy1.enemies)

        # call an update function that u pass status to check if mario needs to move
        # without any input to resemble gravity
