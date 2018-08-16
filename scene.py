""" Defining the base background scene """


class Scene:
    """ Making a matrix to represent the game scene """

    def __init__(self, length, width):
        """ Initial matrix """
        self.length = length
        self.width = width
        self.score = 0
        self.scenematrix = []
        # scenematrix is a matrix to display all elements
        for x in range(0, length):
            self.scenematrix.append([])
            for y in range(0, width):
                self.scenematrix[x].append(' ')

        for x in range(36, length):
            for y in range(0, width):
                self.scenematrix[x][y] = '#'

    def displayScene(self):
        """ Print the screen to the terminal """

        sceneprint = ""
        sceneprint += " "*30 + "SUPER MARIO\n"
        sceneprint += "Score : " + str(self.score) + "\n"
        for i in range(0, self.length):
            for j in range(0, self.width):
                sceneprint += self.scenematrix[i][j]
            sceneprint += '\n'
        sceneprint += "Press Q to exit\n"

        return sceneprint

    def returnmatrix(self):
        return self.scenematrix

    def updatescene(self, updmatrix):
        self.scenematrix = updmatrix
