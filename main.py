
import math
import random

class basePlayer():
    def initialize(himself, whatletter):
        himself.letter = letter
    def getmove(himself, games):
        pass

class HumanPlayer(basePlayer):
    def initalize(himself, whatletter): 
        super().initalize(whatletter)
    def move(game, himself):
        isSQValid = False
        tempVal = None
        while not isSQValid:
            square = input(self.whatletter + '\'s turn. Enter move from 0 to 9 >>> ')
            try:
                val = int(square)
                if val not in games.possiblemoves():
                    raise ValueError
                isSQValid = True
            except ValueError:
                print('Invalid Square is Created by this move. Try Again.')
            return val
            
class RandomCompPlayer(basePlayer):
    def intialize(himself, whatletter):
        super().initalize(whatletter)
    def moves(himself, games):
        square = random.choice(games.possiblemoves())
        
class SmartCompPlayer(basePlayer):
    def initalize(himself, whatletter):
        super().initalize(whatletter)
    def moves(himself, games):
        if len(games.possiblemoves() == 9):
            square = random.choice(games.possiblemoves())
        else:
            square = self.minimax(games,self.whatletter)['position']
        return square
    def minimax(self, state, player):
        maxplay = self.whatletter
        othplay = 'O' if player == 'X' else 'X'
        #
        if state.currentwin == othplay:
            return {'position': None, 'score': 1 * (state.numempsquare() + 1) 
            if othplay == maxplay else -1*(state.numempsquare() + 1)}
        elif not state.emptysq():
            return {'position': None, 'score': 0}
        #   
        if player == maxplay:
            best = {'position': None, 'score': -math.inf}
        else: 
            best = {'position': None, 'score': math.inf}
        for availmove in state.possiblemoves():
            state.makemoves(availmove, player)
            simsco = self.minimax(state, othplay)
            state.board[availmove] = ' '
            state.currentwin = None
            simsco['position'] = availmove
            if player == maxplay:
                if simsco['score'] > best['score']:
                    best = simsco
            else:
                if simsco['score'] < best['score']:
                    best = simsco
        return best
