''' Contains all obstacle class definitions '''
from gamefunctions import *
from config import *


def putcoins(scene, level, coins):
    ''' Put coins on the map according to the level '''
    coin = Coins()
    Coins.coins.append(coin)
    coin.setPos(scene, groundx-6-coin.length, 34)

    coin = Coins()
    Coins.coins.append(coin)
    coin.setPos(scene, groundx-15-coin.length, 44)

    coin = Coins()
    Coins.coins.append(coin)
    coin.setPos(scene, groundx-8-coin.length, 173)

    coin = Coins()
    Coins.coins.append(coin)
    coin.setPos(scene, groundx-8-coin.length, 214)

    coin = Coins()
    Coins.coins.append(coin)
    coin.setPos(scene, groundx-7-coin.length, 234)

    coin = Coins()
    Coins.coins.append(coin)
    coin.setPos(scene, groundx-19-coin.length, 303)

    coin = Coins()
    Coins.coins.append(coin)
    coin.setPos(scene, groundx-20-coin.length, 448)

    if level >= 2:
        coin = Coins()
        Coins.coins.append(coin)
        coin.setPos(scene, groundx-10-coin.length, 193)

        coin = Coins()
        Coins.coins.append(coin)
        coin.setPos(scene, groundx-13-coin.length, 261)

        coin = Coins()
        Coins.coins.append(coin)
        coin.setPos(scene, groundx-10-coin.length, 275)

        coin = Coins()
        Coins.coins.append(coin)
        coin.setPos(scene, groundx-27-coin.length, 308)

        coin = Coins()
        Coins.coins.append(coin)
        coin.setPos(scene, groundx-19-coin.length, 408)

    if level >= 3:
        coin = Coins()
        Coins.coins.append(coin)
        coin.setPos(scene, groundx-10-coin.length, 398)

        coin = Coins()
        Coins.coins.append(coin)
        coin.setPos(scene, groundx-27-coin.length, 418)

        coin = Coins()
        Coins.coins.append(coin)
        coin.setPos(scene, groundx-10-coin.length, 435)

        coin = Coins()
        Coins.coins.append(coin)
        coin.setPos(scene, groundx-25-coin.length, 473)


def update_coins(scene, level, coins):
    print(Coins.coins)
    for coin in Coins.coins:
        coin.setPos(scene, coin.x, coin.y)


def collect_coin(scene, y, coins):
    ''' Delete the coin after collecting it '''
    scenematrix = scene.returnmatrix()
    for coin in Coins.coins:
        if coin.y in range(y-4, y+4):
            for i in range(coin.x, coin.x+coin.length):
                for j in range(coin.y, coin.y+coin.width):
                    scenematrix[i][j] = ' '
        Coins.coins.remove(coin)
        Coins.collected += 1
        del coin
        break
    scene.updatescene(scenematrix)


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


class Coins(Obstacle):
    ''' Coins that can be collected as the player moves over them'''
    coins = []
    collected = 0

    def __init__(self, length=3, width=3):
        Obstacle.__init__(self, length, width)
        self.x = 0
        self.y = 0
        p = colors['Yellow'] + '$' + RESET
        self.matrix = [[' ', p, ' '],
                       [p, p, p],
                       [' ', p, ' ']]

    def put_coin(scene, x, y):
        coin = Coins()
        coin.setPos(scene, x, y)
