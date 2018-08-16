""" Defining the characterstics of the player and enemies """
from gamefunctions import *


class Person:
    """ Base definition of people involved in the game"""

    def __init__(self, length, width):
        """ Giving initial standard values """

        self.length = length
        self.width = width

        # x and y are the values of the top left coordinate
        self.x = None
        self.y = None
        self.matrix = []

        # defining how much the person moves at a time
        self.step = None
        self.jump = None

    def setPos(self, scene, x, y):
        blitobject(scene, self, x, y)
        self.x = x
        self.y = y

    def moveleft(self, scene):
        self.setPos(scene, self.x, self.y - self.step)

    def moveright(self, scene):
        self.setPos(scene, self.x, self.y + self.step)

    def jumpup(self, scene):
        self.setPos(scene, self.x - self.jump, self.y + self.step)

    def returnmatrix(self):
        """ Return the person as a matrix """
        return self.matrix


class Mario(Person):
    """ Defining the classic hero """

    def __init__(self, length, width):
        """ Initialize Mario as a person and give initial structure"""
        Person.__init__(self, length, width)
        self.matrix = [[' ', chr(213), ' '], [
            '/', '|', '\\'], [' ', '|', ' '], ['/', ' ', '\\']]
        self.step = 2
        self.jump = 4
        self.x = 32
        self.y = 4

    def move(self, keypress, scene):
        """ Functionality to move mario according to user input """

        if keypress == 'w':
            self.jumpup(scene)
        elif keypress == 'a':
            self.moveleft(scene)
        elif keypress == 'd':
            self.moveright(scene)
