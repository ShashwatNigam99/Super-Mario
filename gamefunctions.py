""" Define functions like:
 1. Blitting objects/people on to the scene matrix
 2. Checking collisions
"""


def blitobject(scene, item, x, y):
    """ Blit given item over the scene specified """

    scenematrix = scene.returnmatrix()
    itemmatrix = item.returnmatrix()
    k = 0
    l = 0
    for i in range(item.x, item.x + item.length):
        for j in range(item.y, item.y + item.width):
            scenematrix[i][j] = ' '
    for i in range(x, x + item.length):
        for j in range(y, y + item.width):
            scenematrix[i][j] = itemmatrix[i-x][j-y]
    scene.updatescene(scenematrix)
