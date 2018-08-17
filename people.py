""" Defining the characterstics of the player and enemies """
from gamefunctions import *
from input import *
import os

getinp = Get()


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
    # status : 0 - ground , 1air

    def moveleft(self, scene):
        if self.status == 0:
            if(clashcheck(scene, self, self.x, self.y - self.step) == 0):
                self.setPos(scene, self.x, self.y - self.step)
        else:
            if(clashcheck(scene, self, self.x + self.jump, self.y - self.step) == 0):
                self.setPos(scene, self.x + (self.gravity), self.y - self.step)

    def moveright(self, scene):
        if self.status == 0:
            if(clashcheck(scene, self, self.x, self.y + self.step) == 0):
                self.setPos(scene, self.x, self.y + self.step)
        else:
            if(clashcheck(scene, self, self.x + self.jump, self.y + self.step) == 0):
                self.setPos(scene, self.x + (self.gravity), self.y + self.step)

    def jumpup(self, scene):
        # has to be on the ground to be allowed to jump
        if self.status == 0:
            if(clashcheck(scene, self, self.x - self.jump*2, self.y) == 0):
                self.setPos(scene, self.x - self.jump*2, self.y)
                self.status = 1
        '''     os.system('clear')
                print(scene.displayScene())
                input = input_to(getinp)  # calling input for a parabolic jump
                if input is not None:
                    # self.status = 2
                    if(input == 'w'):
                        if(clashcheck(scene, self, self.x-self.jump, self.y) == 0):
                            self.setPos(scene, self.x - self.jump, self.y)
                    if(input == 'a'):
                        if(clashcheck(scene, self, self.x-self.jump, self.y-self.step) == 0):
                            self.setPos(scene, self.x-self.jump,
                                        self.y-self.step)
                    if(input == 'd'):
                        if(clashcheck(scene, self, self.x-self.jump, self.y+self.step) == 0):
                            self.setPos(scene, self.x-self.jump,
                                        self.y+self.step)
                else:
                    self.gravityfall(scene)'''

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
        self.step = 4
        self.jump = 8
        self.x = 32
        self.y = 4
        # setting status to be equal to 0
        # 0-on ground,1- in air going down ,2 - in air going up
        self.status = 0
        self.gravity = 1

    def move(self, keypress, scene):
        """ Functionality to move mario according to user input """

        if keypress == 'w':
            self.jumpup(scene)
        elif keypress == 'a':
            self.moveleft(scene)
        elif keypress == 'd':
            self.moveright(scene)

    def gravityfall(self, scene):

        if self.status == 1:
            if(clashcheck(scene, self, self.x + self.gravity, self.y) == 0):
                self.setPos(scene, self.x+self.gravity, self.y)
