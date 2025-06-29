import javax.swing.*;
import java.awt.*;
public class GUI {
    private JFrame frame;
    private JPanel gameBoardPanel;
    private JButton[][] gameBoardButtons;
    private GameLogic gameLogic;
    public GUI() {
        frame = new JFrame("Strategic Moves");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Set up the game board panel
        gameBoardPanel = new JPanel(new GridLayout(GameLogic.BOARD_SIZE, GameLogic.BOARD_SIZE));
        frame.add(gameBoardPanel);
        // Create game board buttons
        gameBoardButtons = new JButton[GameLogic.BOARD_SIZE][GameLogic.BOARD_SIZE];
        for (int row = 0; row < GameLogic.BOARD_SIZE; row++) {
            for (int col = 0; col < GameLogic.BOARD_SIZE; col++) {
                gameBoardButtons[row][col] = new JButton();
                gameBoardPanel.add(gameBoardButtons[row][col]);
            }
        }
        // Set up other necessary components and player options
        frame.pack();
        frame.setVisible(true);
        // Initialize game logic
        gameLogic = new GameLogic(gameBoardButtons);
    }
    public void startGame() {
        // Start the game loop
        // Allow players to make moves, update the game board, etc.
        for (int row = 0; row < GameLogic.BOARD_SIZE; row++) {
            for (int col = 0; col < GameLogic.BOARD_SIZE; col++) {
                final int r = row;
                final int c = col;
                gameBoardButtons[row][col].addActionListener(e -> {
                    gameLogic.makeMove(r, c);
                });
            }
        }
    }
}