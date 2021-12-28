import math
import time
from main import HumanPlayer, RandomCompPlayer, SmartCompPlayer

class TTT():
    def initalize(self):
        self.board = self.createb()
        self.currentwinner = None
        
    @staticmethod
    def makeb(): 
        return [' ' for _ in range(9)]
        
    def printb(self):
        for row in [self.board[i*3:(i+1) *3] for i in range(3)]:
            print('| ' + '|'.join(row) + '|')
    
    @staticmethod
    def printbnums():
        numb = [[str(i) for i in range(j*3, (j+1) * 3)] for j in range(3)]
        for row in numb:
            print('|' + '|'.join(row) + '|')
            
    def makemov(self, sq, whatletter):
        if self.board[sq] == ' ':
            self.board[sq] = whatletter
            if self.winner(sq, whatletter):
                self.currentwinner = whatletter
            return True
        return False
    
    def winner(self, sq, whatletter):
        rindex = math.floor(sq/3)
        row = self.board[rindex*3: (rindex + 1)*3]
        if all([s == whatletter for s in row]):
            return True
        cindex = sq%3
        column = self.board[cindex+i*3 for i in range(3)]
        if all([s == whatletter for s in column]):
            return True
        if sq % 2 == 0:
            diag1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == whatletter for s in diag1]):
                return True
            diag2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == whatletter for s in diag2]):
                return True
        return False
    
    def emptysq(self):
        return ' ' in self.board
        
    def numemptysq(self):
        return self.board.count(' ')
    
    def possiblemoves(self):
        return [i for i, x in enumerate(self.board) if x == " "]
        
    def play(games, oplay, xplay, printg = True):
        if printg:
            games.printbnums()
        
        whatletter = 'X'
        while game.emptysq():
            if whatletter == 'O':
                sq = oplay.getmove(games)
            else:
                sq = xplay.getmove(games)
            if game.makemov(sq, whatletter):
                if printg:
                    print(whatletter + 'makes a move to square {}'.format(sq))
                    games.printb()
                    print('')
                if game.currentwinner:
                    if printg:
                        print(whatletter + ' wins!')
                    return whatletter
                whatletter = 'O' if whatletter == 'X' else 'X'
            time.sleep(.8)
        if printg:
            print('It\'s a tie!')
            
    if __name__ == '__main__':
        xplay = SmartCompPlayer('X')
        oplay = HumanPlayer('O')
        t = TTT()
        play(t, xplay, oplay, printg = True)
    
