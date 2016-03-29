class GameBoard:

    def __init__(self):

    	"""
    	Initialization method of 3x3 GameBoard class
    	"""
        
        self.gameBoard = [[' ' for x in range(3)] for x in range(3)]

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
        
        # top row
	if (self.gameBoard[0][0] == playerIdentity and self.gameBoard[0][1] == 
		playerIdentity and self.gameBoard[0][2] == playerIdentity):
			return true
	
       	# middle row
       	elif (self.gameBoard[1][0] == playerIdentity and self.gameBoard[1][1] == 
		playerIdentity and self.gameBoard[1][2] == playerIdentity):
	      		return true
	
	# bottom row
	elif (self.gameBoard[2][0] == playerIdentity and self.gameBoard[2][1] == 
		playerIdentity and self.gameBoard[2][2] == playerIdentity):
	       		return true
	
        
       	# Vertical Testing:

	# left row
	elif (self.gameBoard[0][0] == playerIdentity and self.gameBoard[1][0] == 
		playerIdentity and self.gameBoard[2][0] == playerIdentity):
	       		return true
	
	# middle row
	elif (self.gameBoard[0][1] == playerIdentity and self.gameBoard[1][1] == 
		playerIdentity and self.gameBoard[2][1] == playerIdentity):
				return true
	
	# right row
	elif (self.gameBoard[0][2] == playerIdentity and self.gameBoard[1][2] == 
		playerIdentity and self.gameBoard[2][2] == playerIdentity):
	       		return true
	

	# Diagonal Testing:

	# Left-Right
	elif (self.gameBoard[0][0] == playerIdentity and self.gameBoard[1][1] == 
		playerIdentity and self.gameBoard[2][2] == playerIdentity):
	       		return true
	
	# Right-Left
	elif (self.gameBoard[0][2] == playerIdentity and self.gameBoard[1][1] == 
		playerIdentity and self.gameBoard[2][0] == playerIdentity):
	       		return true
	
	return false

