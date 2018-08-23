""" Defining the base background scene """
from config import *


class Scene:
    """ Making a matrix to represent the game scene """

    def __init__(self, length, width, fullwidth):
        """ Initial matrix """
        self.start = 0
        self.length = length
        self.width = width
        self.fullwidth = fullwidth
        self.max_y = 0
        self.score = 0
        self.scenematrix = []
        # scenematrix is a matrix to display all elements
        for x in range(0, fullwidth):
            self.scenematrix.append([])
            for y in range(0, fullwidth):
                self.scenematrix[x].append(' ')
        for x in range(groundx, length):
            for y in range(0, fullwidth):
                self.scenematrix[x][y] = colors['Brown'] + '#' + RESET

    def displayScene(self, level):
        """ Print the screen to the terminal """

        sceneprint = ""
        sceneprint += colors['Yellow'] + " "*40 + "SUPER MARIO\n" + RESET
        sceneprint += colors['Cyan']+"SCORE : " +\
            str(self.score) + " "*30+"LEVEL:"+str(level) + " "*30 + \
            "LIVES:" + str(Lives.lives)+"\n"+RESET
        if self.start >= self.fullwidth - self.width:
            self.start = self.fullwidth - self.width
        for i in range(0, self.length):
            for j in range(self.start, self.start + self.width):
                sceneprint += str(self.scenematrix[i][j])
            sceneprint += '\n'
        sceneprint += "Press Q to exit\n"
        return sceneprint

    def returnmatrix(self):
        return self.scenematrix

    def updatescene(self, updmatrix):
        self.scenematrix = updmatrix
