''' Contains all obstacle class definitions '''
from gamefunctions import *


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
        self.matrix = [['/', '\\', '/', '\\', '/', '\\'],
                       ['\\', ' ', ' ', ' ', ' ', '/'],
                       [' ', '\\', '/', '\\', '/', ' ']]


class Grass(Obstacle):
    '''Background Mountains'''

    def __init__(self, length, width):
        ''' Initialize as a type of obstacke '''
        Obstacle.__init__(self, length, width)
        self.x = 0
        self.y = 0
        self.matrix = [[' ', '*', ' '],
                       ['*', '*', '*']]


# class Walls(Obstacle):
