package org.kingswoodoxford;

public class GameBoard {

	public char[][] gameBoard = new char[3][3];

	// test the game board for an x win
	public boolean testWinX(char[][] gameBoard) {

		// Horizontal Testing:

		// top row
		if (gameBoard[0][0] == 'x' && gameBoard[0][1] == 'x' && gameBoard[0][2] == 'x') {
			return true;
		}
		// middle row
		if (gameBoard[1][0] == 'x' && gameBoard[1][1] == 'x' && gameBoard[1][2] == 'x') {
			return true;
		}
		// bottom row
		if (gameBoard[2][0] == 'x' && gameBoard[2][1] == 'x' && gameBoard[2][2] == 'x') {
			return true;
		}

		// Vertical Testing:

		// left row
		if (gameBoard[0][0] == 'x' && gameBoard[1][0] == 'x' && gameBoard[2][0] == 'x') {
			return true;
		}
		// middle row
		if (gameBoard[0][1] == 'x' && gameBoard[1][1] == 'x' && gameBoard[2][1] == 'x') {
			return true;
		}
		// right row
		if (gameBoard[0][2] == 'x' && gameBoard[1][2] == 'x' && gameBoard[2][2] == 'x') {
			return true;
		}

		// Diagonal Testing:

		// Left-Right
		if (gameBoard[0][0] == 'x' && gameBoard[1][1] == 'x' && gameBoard[2][2] == 'x') {
			return true;
		}
		// Right-Left
		if (gameBoard[0][2] == 'x' && gameBoard[1][1] == 'x' && gameBoard[2][0] == 'x') {
			return true;
		}

		return false;
	}

	// Test the game board for an O win
	public boolean testWinO(char[][] gameBoard) {
		// Horizontal Testing:

		// top row
		if (gameBoard[0][0] == 'o' && gameBoard[0][1] == 'o' && gameBoard[0][2] == 'o') {
			return true;
		}
		// middle row
		if (gameBoard[1][0] == 'o' && gameBoard[1][1] == 'o' && gameBoard[1][2] == 'o') {
			return true;
		}
		// bottom row
		if (gameBoard[2][0] == 'o' && gameBoard[2][1] == 'o' && gameBoard[2][2] == 'o') {
			return true;
		}

		// Vertical Testing:

		// left row
		if (gameBoard[0][0] == 'o' && gameBoard[1][0] == 'o' && gameBoard[2][0] == 'o') {
			return true;
		}
		// middle row
		if (gameBoard[0][1] == 'o' && gameBoard[1][1] == 'o' && gameBoard[2][1] == 'o') {
			return true;
		}
		// right row
		if (gameBoard[0][2] == 'o' && gameBoard[1][2] == 'o' && gameBoard[2][2] == 'o') {
			return true;
		}

		// Diagonal Testing:

		// Left-Right
		if (gameBoard[0][0] == 'o' && gameBoard[1][1] == 'o' && gameBoard[2][2] == 'o') {
			return true;
		}
		// Right-Left
		if (gameBoard[0][2] == 'o' && gameBoard[1][1] == 'o' && gameBoard[2][0] == 'o') {
			return true;
		}

		return false;
	}

	
	
}
