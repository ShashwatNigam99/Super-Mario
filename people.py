""" Defining the characterstics and functions of the player and enemies """
from gamefunctions import *
from input import *
from config import *
import os
import random

getinp = Get()


def putenemies(scene, level, enemies):
    """ Put enemies onto the scene according to the level """
    bot = Enemy1(random.randint(1, 3)*2, random.randint(2, 4)*2, 160, 180)
    Enemy1.enemies.append(bot)
    bot.setPos(scene, groundx-bot.length, bot.lpos)

    bot = Enemy1(random.randint(1, 3)*2, random.randint(2, 4)*2, 202, 225)
    Enemy1.enemies.append(bot)
    bot.setPos(scene, groundx-bot.length, bot.lpos)

    bot = Enemy1(random.randint(1, 2)*2, random.randint(1, 3)*2, 390, 410)
    Enemy1.enemies.append(bot)
    bot.setPos(scene, groundx-bot.length-10, bot.lpos)

    bot = Enemy1(random.randint(1, 2)*2, random.randint(1, 3)*2, 430, 450)
    Enemy1.enemies.append(bot)
    bot.setPos(scene, groundx-bot.length-10, bot.lpos)

    if level >= 2:
        bot = Enemy1(random.randint(1, 2)*2, random.randint(1, 3)*2,
                     288, 304)
        Enemy1.enemies.append(bot)
        bot.setPos(scene, groundx-bot.length-19, bot.lpos)

        bot = Enemy1(random.randint(1, 2)*2, random.randint(1, 3)*2,
                     300, 316)
        Enemy1.enemies.append(bot)
        bot.setPos(scene, groundx-bot.length-27, bot.lpos)

        bot = Enemy1(random.randint(1, 2)*2, random.randint(1, 3)*2,
                     63, 95)
        Enemy1.enemies.append(bot)
        bot.setPos(scene, groundx-bot.length-9, bot.lpos)

    if level >= 3:
        bot = Enemy1(random.randint(1, 2)*2, random.randint(1, 3)*2,
                     400, 416)
        Enemy1.enemies.append(bot)
        bot.setPos(scene, groundx-bot.length-18, bot.lpos)

        bot = Enemy1(random.randint(1, 2)*2, random.randint(1, 3)*2,
                     440, 456)
        Enemy1.enemies.append(bot)
        bot.setPos(scene, groundx-bot.length-20, bot.lpos)

        bot = Enemy1(random.randint(1, 2)*2, random.randint(1, 3)*2,
                     410, 426)
        Enemy1.enemies.append(bot)
        bot.setPos(scene, groundx-bot.length-20, bot.lpos)


def update_enemies(scene, level, enemies):
    """ Update enemy positions, called in each game loop iteration """
    for bot in Enemy1.enemies:
        if bot.direction == 1:
            bot.setPos(scene, bot.x, bot.y + bot.step)
        elif bot.direction == -1:
            bot.setPos(scene, bot.x, bot.y - bot.step)
        if(bot.y >= bot.rpos or bot.y <= bot.lpos):
            bot.direction *= -1


def killenemy(scene, y, enemies):
    """ Kills the enemy that lies between two coordinates """
    scenematrix = scene.returnmatrix()
    for bot in Enemy1.enemies:
        if(y >= bot.lpos and y <= bot.rpos):
            # clear the bot
            os.system('aplay -q sounds/ohyeah.wav&')
            for i in range(bot.x, bot.x+bot.length):
                for j in range(bot.y, bot.y+bot.width):
                    scenematrix[i][j] = ' '
            Enemy1.enemies.remove(bot)
            # score tracking
            Enemy1.killed += 1
            del bot
            break
    scene.updatescene(scenematrix)


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
        """ Calls blitobject function and updates position """
        blitobject(scene, self, x, y)
        self.x = x
        self.y = y

    def moveleft(self, scene):
        """ Make mario move left after making necessary checks """

        if self.status == 0:
            if clashcheck(scene, self, self.x, self.y - self.step) == 0:
                self.setPos(scene, self.x, self.y - self.step)
        else:
            chk = clashcheck(scene, self, self.x +
                             self.gravity, self.y - self.step)
            if chk == 0:
                self.setPos(scene, self.x + self.gravity,
                            self.y - self.step)
            elif chk == 2:
                killenemy(scene, self.y-self.step, Enemy1.enemies)
                self.setPos(scene, self.x + self.gravity,
                            self.y - self.step)
            elif chk == 3:
                killenemy(scene, self.y-self.step, Enemy1.enemies)
                Lives.lives -= 1

                self.setPos(scene, self.x + self.gravity,
                            self.y - self.step)

    def moveright(self, scene):
        """ Make mario move right after making necessary checks """

        if self.status == 0:
            if(clashcheck(scene, self, self.x, self.y + self.step) == 0):
                self.setPos(scene, self.x, self.y + self.step)
        else:
            chk = clashcheck(scene, self, self.x +
                             self.gravity, self.y + self.step)
            if chk == 0:
                self.setPos(scene, self.x + self.gravity,
                            self.y + self.step)
            elif chk == 2:
                killenemy(scene, self.y+self.step, Enemy1.enemies)
                self.setPos(scene, self.x + self.gravity,
                            self.y + self.step)
            elif chk == 3:
                killenemy(scene, self.y+self.step, Enemy1.enemies)
                Lives.lives -= 1
                self.setPos(scene, self.x + self.gravity,
                            self.y + self.step)

    def jumpup(self, scene):
        """ Make mario jump up """
        # has to be on the ground to be allowed to jump
        if self.status == 0:
            os.system('aplay -q sounds/jump.wav&')
            xup = 0
            while(xup < (self.jump*2)):
                if(clashcheck(scene, self, self.x - xup, self.y) == 0):
                    #    self.setPos(scene, (self.x-xup), self.y)
                    xup += 1
                else:
                    break
            self.setPos(scene, (self.x-xup), self.y)
            # jumped = 0
            # print(xup)
            # while jumped <= xup:
            #     print(jumped)
            #     self.setPos(scene, (self.x-jumped), self.y)
            #     jumped += 1
            self.status = 1

    def returnmatrix(self):
        """ Return the person as a matrix """
        return self.matrix


class Mario(Person):
    """ Defining the classic hero """

    def __init__(self, length, width):
        """ Initialize Mario as a person and give initial structure"""
        Person.__init__(self, length, width)
        head = colors['Yellow'] + chr(213) + RESET
        mid = colors['Red'] + '|' + RESET
        left = colors['Purple'] + '/' + RESET
        right = colors['Purple'] + '\\' + RESET

        self.matrix = [[' ', head, ' '], [
            left, mid, right], [' ', mid, ' '], [left, ' ', right]]
        self.step = 2
        self.jump = 6
        self.x = 32
        self.y = 4
        # setting status to be equal to 0
        # 0-on ground, 1- in air going down
        self.status = 0
        self.gravity = 1

    def move(self, keypress, scene):
        """ Functionality to move mario according to user input """
        if keypress == 'w' or keypress == 'A':
            self.jumpup(scene)
        elif keypress == 'a' or keypress == 'D':
            self.moveleft(scene)
        elif keypress == 'd' or keypress == 'C':
            self.moveright(scene)

    def gravityfall(self, scene):
        """ Simple gravity fall if no input is provided and in air"""
        if self.status == 1:
            chk = clashcheck(scene, self, self.x+self.gravity, self.y)
            if chk == 0:
                self.setPos(scene, self.x+self.gravity, self.y)
            elif chk == 2:
                killenemy(scene, self.y, Enemy1.enemies)
                self.setPos(scene, self.x + self.gravity,
                            self.y)
            elif chk == 3:
                killenemy(scene, self.y, Enemy1.enemies)
                Lives.lives -= 1
                self.setPos(scene, self.x + self.gravity,
                            self.y)


class Enemy1(Person):
    ''' Defining a resizable enemy that shuttles between two points '''
    # this list holds all the enemies currently alive on the scene
    enemies = []
    # keeps track of enemies killed
    killed = 0

    def __init__(self, length, width, lpos, rpos):
        """ Define characterstics of Enemy """
        Person.__init__(self, length, width)
        self.lpos = lpos
        self.rpos = rpos
        self.x = 0
        self.y = 0
        self.step = 1
        # 1 for going right and -1 to go left
        self.direction = 1
        self.matrix = []
        self.matrix.append(['^' for i in range(0, width)])
        for i in range(1, length):
            self.matrix.append([])
            for j in range(0, int(width/2)):
                self.matrix[i].append('{')
            for j in range(int(width/2), width):
                self.matrix[i].append('}')
