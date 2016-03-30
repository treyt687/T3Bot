import sys

sys.path.insert(0, '/Users/Trey/Desktop/Code/Python/t3bot/T3/src/')

try:
    import Tkinter
except ImportError:
    print("TKinter not installed. Execute 'pip install python-tk' in terminal.)

import gameBoard

class GamePlay:

    """
    Class for executing a T3Game using Tkinter GUI based OOP
    """

    def __init__(self):
        self.root = Tkinter.Tk()
        root.title("T3Bot")
        self.gb = gameBoard.GameBoard()
        self.initButtons()

    def initButtons(self):

        """
        Function call for initializing GameBoard buttons
        in 3x3 structure
        """

        zz = Tkinter.Button(self.root, text=str(self.gb.gameBoard[0][0]),
            command=lambda: self.callback(0, 0)).grid(row=0,column=0)
        zo = Tkinter.Button(self.root, text=str(self.gb.gameBoard[0][1]),
            command=lambda: self.callback(0, 1)).grid(row=0,column=1)
        zt = Tkinter.Button(self.root, text=str(self.gb.gameBoard[0][2]),
            command=lambda: self.callback(0, 2)).grid(row=0,column=2)
        oz = Tkinter.Button(self.root, text=str(self.gb.gameBoard[1][0]),
            command=lambda: self.callback(1, 0)).grid(row=1,column=0)
        oo = Tkinter.Button(self.root, text=str(self.gb.gameBoard[1][1]),
            command=lambda: self.callback(1, 1)).grid(row=1,column=1)
        ot = Tkinter.Button(self.root, text=str(self.gb.gameBoard[1][2]),
            command=lambda: self.callback(1, 2)).grid(row=1,column=2)
        tz = Tkinter.Button(self.root, text=str(self.gb.gameBoard[2][0]),
            command=lambda: self.callback(2, 0)).grid(row=2,column=0)
        to = Tkinter.Button(self.root, text=str(self.gb.gameBoard[2][1]),
            command=lambda: self.callback(2, 1)).grid(row=2,column=1)
        tt = Tkinter.Button(self.root, text=str(self.gb.gameBoard[2][2]),
            command=lambda: self.callback(2, 2)).grid(row=2,column=2)

    def getRoot(self):
        """
        Encapsulation method for returning TK root
        to execute TK.mainloop()
        """
        return self.root

    def callback(self, r, c):
        """
        Function callback for Tkinter buttons
        on GameBoard -> For some reason not calling
        callback as a lambda executes the callback
        method immediately upon runtime - FIX?
        """
        print("%s, %s") % (r, c)

gp = GamePlay()
gp.getRoot().mainloop()
