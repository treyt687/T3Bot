class GameBoard:

    def __init__(self):

    	"""
    	Initialization method of 3x3 GameBoard class
    	"""
        self.currentTurn = 'x'

        self.gameBoard = [['-' for x in range(3)] for x in range(3)]

    def getCurrentTurn(self):

        """
        Encapsulation method for returning
        the currentTurn of the GameBoard
        """

        return self.currentTurn

    def changeCurrentTurn(self):

        """
        Function call for changing the currentTurn
        on the GameBoard
        """

        if self.currentTurn == 'x':
            self.currentTurn = 'o'
        else:
            self.currentTurn = 'x'

    def placeKey(self, playerTurn, locX, locY):

        """
        Function call for playing on gameBoard location
        of locX, locY


        ex. placeKey(playerIdentity, 2, 1) -> if gameBoard[2][1] is empty
        playerIdentity will be placed
        """

        if playerTurn == 'x':
            if self.gameBoard[locX][locY] == '-':
                 self.gameBoard[locX][locY] = 'x'
                 self.changeCurrentTurn()
            else:
                print("GameBoard location %d, %d full. Please select new\
                location") % (locX, locY)

        elif playerTurn == 'o':
            if self.gameBoard[locX][locY] == '-':
                 self.gameBoard[locX][locY] = 'o'
                 self.changeCurrentTurn()
            else:
                print("GameBoard location %d, %d full. Please select new \
                location") % (locX, locY)
        else:
            print("Player identity invalid. Please select new player identity.")

    def checkWin(self, playerIdentity):

        """
        Function call for checking win state of self.gameBoard

        ex. checkWin('x') -> will return true if 'x' is found
        in any 3 consecutive directions (vertically, horizontally,
        diagonally) on the gameBoard
        """

        # Horizontal testing
        for r in range(3):
            if (self.gameBoard[r][0] == playerIdentity and self.gameBoard[r][1]
                ==	playerIdentity and self.gameBoard[r][2] == playerIdentity):
            		return True


        # Vertical testing
        for c in range(3):
            if (self.gameBoard[0][c] == playerIdentity and self.gameBoard[1][c]
                == playerIdentity and self.gameBoard[2][c] == playerIdentity):
        			return True

        # Diagonal Checking
        if (self.gameBoard[0][0] == playerIdentity and self.gameBoard[1][1] ==
            playerIdentity and self.gameBoard[2][2] == playerIdentity):
                return True

        elif (self.gameBoard[0][2] == playerIdentity and self.gameBoard[1][1] ==
            playerIdentity and self.gameBoard[2][0] == playerIdentity):
                return True

        return False

    def checkTie(self):
        if (self.gameBoard[0][0] != '-' and self.gameBoard[0][1] != '-'
            and self.gameBoard[0][2] != '-' and self.gameBoard[1][0] != '-'
            and self.gameBoard[1][1] != '-' and self.gameBoard[1][2] != '-'
            and self.gameBoard[2][0] != '-' and self.gameBoard[2][1] != '-'
            and self.gameBoard[2][2] != '-'):
                return True
        return False
