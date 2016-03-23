package testing;

import org.kingswoodoxford.GameBoard;
import javax.swing.*;
import java.awt.EventQueue;
import java.awt.GridLayout;

@SuppressWarnings("serial")
public class BoardTest extends JFrame {

	static GameBoard newBoard = new GameBoard();
	
	public BoardTest() {
		initUI();
	}
	
	private void initUI() {
		setTitle("Board Test");
        setSize(300, 300);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        
        JPanel boardPanel = new JPanel();
        getContentPane().add(boardPanel);
        boardPanel.setLayout(new GridLayout(3,3));
        
        JButton topLeft = new JButton(String.valueOf(newBoard.gameBoard[0][0]));
        boardPanel.add(topLeft);
        
        JButton topMid = new JButton(String.valueOf(newBoard.gameBoard[0][1]));
        boardPanel.add(topMid);
        
        JButton topRight = new JButton(String.valueOf(newBoard.gameBoard[0][2]));
        boardPanel.add(topRight);
        
        JButton midLeft = new JButton(String.valueOf(newBoard.gameBoard[1][0]));
        boardPanel.add(midLeft);
        
        JButton midMid = new JButton(String.valueOf(newBoard.gameBoard[1][1]));
        boardPanel.add(midMid);
        
        JButton midRight = new JButton(String.valueOf(newBoard.gameBoard[1][2]));
        boardPanel.add(midRight);
        
        JButton bottomLeft = new JButton(String.valueOf(newBoard.gameBoard[2][0]));
        boardPanel.add(bottomLeft);
        
        JButton bottomMid = new JButton(String.valueOf(newBoard.gameBoard[2][1]));
        boardPanel.add(bottomMid);
        
        JButton bottomRight = new JButton(String.valueOf(newBoard.gameBoard[2][2]));
        boardPanel.add(bottomRight);
	}
	
	public static void main(String[] args) {

        EventQueue.invokeLater(new Runnable() {
        
            @Override
            public void run() {
                BoardTest ex = new BoardTest();
                ex.setVisible(true);
                boolean xTurn = true;
                while (!(newBoard.testWinX(newBoard.gameBoard)) && !(newBoard.testWinO(newBoard.gameBoard))) {
                	// implement turns
                }
            }
        });
    }
}
