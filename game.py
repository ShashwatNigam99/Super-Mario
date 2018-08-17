import os
import sys
from scene import Scene
from people import *
from input import *

scene = Scene(40, 100, 500)
mario = Mario(4, 3)
mario.setPos(scene, 32, 4)

getinp = Get()
print(scene.displayScene())

while True:
    input = input_to(getinp)
    os.system('clear')
    print(scene.displayScene())

    if input is not None:
        curhalf = scene.start+50
        if input in ['w', 'a', 'd']:
            if input == 'd':
                if(mario.y <= curhalf):
                    mario.move(input, scene)
                else:
                    scene.start += 3
                    mario.move(input, scene)
            else:
                mario.move(input, scene)
            # else:
            #     scene.start

        if input == 'q':
            os.system('clear')
            sys.exit()

    else:
        mario.gravityfall(scene)

        # call an update function that u pass status to check if mario needs to move
        # without any input to resemble gravity
