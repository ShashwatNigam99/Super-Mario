import os
import sys
from scene import Scene
from people import *
from input import *

scene = Scene(40, 120)
mario = Mario(4, 3)
mario.setPos(scene, 32, 4)

getinp = Get()
print(scene.displayScene())

while True:
    input = input_to(getinp)
    os.system('clear')
    print(scene.displayScene())

    if input is not None:

        if input in ['w', 'a', 'd']:
            mario.move(input, scene)

        if input == 'q':
            os.system('clear')
            sys.exit()

    else:
        mario.gravityfall(scene)

        # call an update function that u pass status to check if mario needs to move
        # without any input to resemble gravity
