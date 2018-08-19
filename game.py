import os
import sys
from scene import Scene
from people import *
from obstacles import *
from levels import *
from input import *

scene = Scene(40, 100, 500)
mario = Mario(4, 3)
mario.setPos(scene, 32, 4)

generatescene(scene, 1)

# cloud1 = []
# or i in range()
getinp = Get()
print(scene.displayScene())

while True:
    input = input_to(getinp)
    os.system('clear')
    generatescene(scene, 1)
    print(scene.displayScene())

    if input is not None:
        curhalf = scene.start + 70
        if input in ['w', 'a', 'd']:
            if input == 'd':
                if(mario.y <= curhalf):
                    mario.move(input, scene)
                else:
                    scene.start += mario.step
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
