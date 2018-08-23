''' Contains all obstacle class definitions '''
from gamefunctions import *
from config import *


class Obstacle:
    ''' Base definition for any obstacle '''

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.x = None
        self.y = None
        self.matrix = []

    def setPos(self, scene, x, y):
        blitobject(scene, self, x, y)
        self.x = x
        self.y = y

    def returnmatrix(self):
        """ Return the obstacle as a matrix """
        return self.matrix


class Cloud(Obstacle):
    '''Making clouds on top '''

    def __init__(self, length, width):
        ''' Initialize as a type of obstacke '''
        Obstacle.__init__(self, length, width)
        self.x = 0
        self.y = 0
        p = colors['White']+'/'+RESET
        q = colors['White']+'\\'+RESET
        self.matrix = [[p, q, p, q, p, q],
                       [q, ' ', ' ', ' ', ' ', p],
                       [' ', q, p, q, p, ' ']]


class Grass(Obstacle):
    '''Background Mountains'''

    def __init__(self, length, width):
        ''' Initialize as a type of obstacke '''
        Obstacle.__init__(self, length, width)
        self.x = 0
        self.y = 0
        g = colors['Light Green']+'*'+RESET
        self.matrix = [[' ', g, ' '],
                       [g, g, g]]


class Wall(Obstacle):
    ''' Walls that player has to jump '''

    def __init__(self, length, width):
        ''' Initialize as a type of obstacke '''
        Obstacle.__init__(self, length, width)
        self.x = 0
        self.y = 0
        self.matrix = [[colors['Brown']+'#'+RESET for i in range(0, width)]
                       for j in range(0, length)]

    def draw_wall(scene, length, width, y):
        wall = Wall(length, width)
        x = groundx-wall.length
        wall.setPos(scene, x, y)


class Pit(Obstacle):
    ''' Pits that player has to avoid '''

    def __init__(self, length, width):
        ''' Initialize as a type of obstacke '''
        Obstacle.__init__(self, length, width)
        self.x = 0
        self.y = 0
        self.matrix = [[colors['Blue']+'~' for i in range(0, width)]
                       for j in range(0, length)]

    def draw_pit(scene, width, y):
        pit = Pit(scene.length-groundx, width)
        pit.setPos(scene, groundx, y)
