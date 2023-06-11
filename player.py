import math
import random

class player:
    def __init__(self,letter):
    #letter is x or o
        self.letter=letter

    #next move
    def getmove(self,game):
        pass

class NPC(player):
    def __init__(self,letter):
        super().__init__(letter)

    def getmove(self,game):
        #random valid spot
        square = random.choice(game.availablemoves())
        return square

class HumanPlayer(player):
    def _init_ (self,letter):
        super().__init__(letter)

    def getmove(self, game):
        validsquare= False
        value = None
        while not validsquare:
            square = input(self.letter + '\'s turn. input 0-8:')
            #correct value test
            try:
                value = int(square)
                if value not in game.availablemoves():
                    raise ValueError
                validsquare=True
            except ValueError:
                print('Try again. Not valid square')
        return value


