class GameBoard:

    def __init__(self):

    	"""
    	Initialization method of 3x3 GameBoard class
    	"""

        self.gameBoard = [['-' for x in range(3)] for x in range(3)]

    def placeKey(self, playerTurn, locX, locY):

        """
        Function call for playing on gameBoard location
        of locX, locY


        ex. placeKey(playerIdentity, 2, 1) -> if gameBoard[2][1] is empty
        playerIdentity will be placed
        """

        if playerTurn == playerIdentity:
            if self.gameBoard[locX][locY] == ' ':
                 self.gameBoard[locX][locY] = playerIdentity
            else:
                print("GameBoard location %d, %d full. Please select new location") % (locX, loxY)

        elif playerTurn == 'o':
            if self.gameBoard[locX][locY] == ' ':
                 self.gameBoard[locX][locY] = 'o'
            else:
                print("GameBoard location %d, %d full. Please select new location") % (locX, loxY)
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
            if (self.gameBoard[r][0] == playerIdentity and self.gameBoard[r][1] ==
            	playerIdentity and self.gameBoard[r][2] == playerIdentity):
            		return true


        # Vertical testing
        for c in range(3):
            if (self.gameBoard[0][c] == playerIdentity and self.gameBoard[1][c] ==
        		playerIdentity and self.gameBoard[2][c] == playerIdentity):
        			return true

        # Diagonal Checking
        if (self.gameBoard[0][0] == playerIdentity and self.gameBoard[1][1] ==
            playerIdentity and self.gameBoard[2][2] == playerIdentity):
                return true

        elif (self.gameBoard[0][2] == playerIdentity and self.gameBoard[1][1] ==
            playerIdentity and self.gameBoard[2][0] == playerIdentity):
                return true
