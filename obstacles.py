''' Contains all obstacle class definitions '''


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


class Cloud1:
    ''' Type 1 cloud'''

    def __init__(self, length, width):
        ''' Initialize as a type of obstacke '''
        Obstacle.__init__(self, length, width)
        self.matrix = [['/', '\\', '/', '\\', '/', '\\'],
                       ['\\', ' ', ' ', ' ', ' ', '/'],
                       [' ', '\\', '/', '\\', '/', ' ']]
