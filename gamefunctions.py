""" Define functions like:
 1. Blitting objects/people on to the scene matrix
 2. Checking collisions
"""
import os
import sys
from config import *


def check_lives(lives):
    if lives <= 0:
        print(Fore.RED+Style.BRIGHT+" You lost all lives. Final score : " +
              str(scene.score))
        sys.exit()


def clashcheck(scene, item, x, y):
    """ Check if the object clashes with barriers in its updated position.
    Return value : 0 if okay to move, 1 if can't move,
    2 if dead, 3 if collision with enemy """

    if(y > scene.fullwidth-10):
        os.system('aplay -q sounds/gameover.wav&')
        print(" You won ! . Final score : " + str(scene.score))
        sys.exit()
    scenematrix = scene.returnmatrix()

    # check left boundary of item
    if y <= scene.start:
        return 1
    for i in range(x, x + item.length):
        if(i >= scene.length):
            return 1
    for i in range(x, x + item.length):
        if scenematrix[i][y] in killers:
            if scenematrix[i][y] in ['{', '}']:
                print("called")
                return 3
            else:
                print(" You died . Final score : " + str(scene.score))
                os.system('aplay -q sounds/death.wav&')
                sys.exit()
    for i in range(x, x + item.length):
        if scenematrix[i][y] in barriers:
            return 1

    # check right boundary of item
    if y >= scene.fullwidth:
        return 1

    for i in range(x, x + item.length):
        if scenematrix[i][y + item.width - 1] in killers:
            if scenematrix[i][y+item.width-1] in ['{', '}']:
                print("called")
                return 3
            else:
                print(" You died . Final score : " + str(scene.score))
                os.system('aplay -q sounds/death.wav&')
                sys.exit()
    for i in range(x, x + item.length):
        if scenematrix[i][y + item.width - 1] in barriers:
            return 1

    # check top
    for i in range(y, y + item.width):
        if(x <= 0):
            return 1
        elif scenematrix[x][i] in barriers:
            item.status = 1
            return 1

    # check bottom
    for i in range(y, y + item.width):
        if scenematrix[x + item.length - 1][i] in barriers:
            return 1
    for i in range(y, y + item.width):
        if scenematrix[x+item.length-1][i] in beaters:
            return 2
    for i in range(y, y + item.width):
        if scenematrix[x + item.length - 1][i] in killers:
            if scenematrix[x+item.length-1][i] in ['{', '}']:
                return 3
            else:
                print(" You died . Final score : " + str(scene.score))
                os.system('aplay -q sounds/death.wav&')
                sys.exit()
    for i in range(y, y + item.width):
        if scenematrix[x + item.length][i] in barriers:
            item.status = 0
            # reached ground / some platform
    p = 0
    for i in range(y, y + item.width):
        if scenematrix[x + item.length][i] not in barriers:
            p += 1
    if p == 3:
        item.status = 1
    for i in range(y, y + item.width):
        if scenematrix[x+item.length][i] in beaters:
            return 2
    return 0


def blitobject(scene, item, x, y):
    """ Blit given item over the scene where specified
    after deleting previous instance"""
    scenematrix = scene.returnmatrix()
    itemmatrix = item.returnmatrix()
    k = 0
    l = 0
    # deleting previous position
    for i in range(item.x, item.x + item.length):
        for j in range(item.y, item.y + item.width):
            scenematrix[i][j] = ' '
    # putting at new position
    for i in range(x, x + item.length):
        for j in range(y, y + item.width):
            scenematrix[i][j] = itemmatrix[i-x][j-y]
    scene.updatescene(scenematrix)
