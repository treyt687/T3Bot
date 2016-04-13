import sys

sys.path.insert(0, '/Users/Trey/Desktop/Code/Python/t3bot/T3/src/')

import Tkinter


import gameBoard

class GamePlay:

    """
    Class for executing a T3Game using Tkinter GUI based OOP
    """

    def __init__(self):
        self.root = Tkinter.Tk()
        self.root.title("T3Bot")
        self.root.minsize(width=300, height=300)
        self.root.maxsize(width=300, height=300)
        self.window_width = self.root.winfo_height()
        self.window_height = self.root.winfo_width()
        self.gb = gameBoard.GameBoard()
        self.updateButtons()

    def updateButtons(self):

        """
        Function call for initializing GameBoard buttons
        in 3x3 structure
        """

        self.zz = Tkinter.Button(self.root, text=str(self.gb.gameBoard[0][0]),
            command=lambda: self.play(0, 0)).grid(row=0,column=0)
        self.zo = Tkinter.Button(self.root, text=str(self.gb.gameBoard[0][1]),
            command=lambda: self.play(0, 1)).grid(row=0,column=1)
        self.zt = Tkinter.Button(self.root, text=str(self.gb.gameBoard[0][2]),
            command=lambda: self.play(0, 2)).grid(row=0,column=2)
        self.oz = Tkinter.Button(self.root, text=str(self.gb.gameBoard[1][0]),
            command=lambda: self.play(1, 0)).grid(row=1,column=0)
        self.oo = Tkinter.Button(self.root, text=str(self.gb.gameBoard[1][1]),
            command=lambda: self.play(1, 1)).grid(row=1,column=1)
        self.ot = Tkinter.Button(self.root, text=str(self.gb.gameBoard[1][2]),
            command=lambda: self.play(1, 2)).grid(row=1,column=2)
        self.tz = Tkinter.Button(self.root, text=str(self.gb.gameBoard[2][0]),
            command=lambda: self.play(2, 0)).grid(row=2,column=0)
        self.to = Tkinter.Button(self.root, text=str(self.gb.gameBoard[2][1]),
            command=lambda: self.play(2, 1)).grid(row=2,column=1)
        self.tt = Tkinter.Button(self.root, text=str(self.gb.gameBoard[2][2]),
            command=lambda: self.play(2, 2)).grid(row=2,column=2)

    def getRoot(self):
        """
        Encapsulation method for returning TK root
        to execute TK.mainloop()
        """
        return self.root

    def play(self, r, c):
        if self.gb.getCurrentTurn() == 'x':
            self.gb.placeKey('x', r, c)
            self.gb.changeCurrentTurn()
        elif self.gb.getCurrentTurn() == 'o':
            self.gb.placeKey('o', r, c)
            self.gb.changeCurrentTurn()


        """
        Function callback for Tkinter buttons
        on GameBoard -> For some reason not calling
        play as a lambda executes the play
        method immediately upon runtime - FIX?
        """
        print("%s, %s") % (r, c)

gp = GamePlay()
gameRunning = True

while (gameRunning):
    gp.updateButtons()
    if gp.gb.checkWin('x') == True:
        gameRunning = False
    elif gp.gb.checkWin('o') == True:
        gameRunning = False
    gp.getRoot().update()
