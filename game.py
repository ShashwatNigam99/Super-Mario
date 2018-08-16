import os
import sys
from scene import Scene
from people import *
from input import *

scene = Scene(40, 80)
mario = Mario(4, 3)
mario.setPos(scene, 32, 4)

getinp = Get()
print(scene.displayScene())

while True:
    input = input_to(getinp)
    os.system('clear')
    print(scene.displayScene())

    if input is not None:
        if input in allowedinputs:
            mario.move(input, scene)
