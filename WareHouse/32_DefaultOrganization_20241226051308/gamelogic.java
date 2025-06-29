import javax.swing.JButton;
public class GameLogic {
    public static final int BOARD_SIZE = 8;
    private char[][] gameBoard;
    private int currentPlayer;
    private boolean gameOver;
    private JButton[][] gameBoardButtons;
    public GameLogic(JButton[][] gameBoardButtons) {
        this.gameBoardButtons = gameBoardButtons;
        gameBoard = new char[BOARD_SIZE][BOARD_SIZE];
        initializeGameBoard();
        currentPlayer = 1;
        gameOver = false;
    }
    private void initializeGameBoard() {
        // Initialize the game board with empty spaces
        for (int i = 0; i < BOARD_SIZE; i++) {
            for (int j = 0; j < BOARD_SIZE; j++) {
                gameBoard[i][j] = ' ';
            }
        }
    }
    /**
     * This method makes a move on the game board.
     *
     * @param row The row index of the move.
     * @param col The column index of the move.
     */
    public void makeMove(int row, int col) {
        // Check if the move is valid
        if (!gameOver && isValidMove(row, col)) {
            // Update the game board with the move
            gameBoard[row][col] = (currentPlayer == 1) ? 'X' : 'O';
            gameBoardButtons[row][col].setText(String.valueOf(gameBoard[row][col]));
            currentPlayer = (currentPlayer == 1) ? 2 : 1;
            if (isGameOver()) {
                gameOver = true;
                System.out.println("Player " + ((currentPlayer == 1) ? 2 : 1) + " wins!");
            } else if (isGameDraw()) {
                gameOver = true;
                System.out.println("The game is a draw!");
            }
        }
    }
    private boolean isValidMove(int row, int col) {
        // Add your logic to check if the move is valid
        // For example, check if the specified position is empty or within the board boundaries
        // Return true if the move is valid, false otherwise
        if (row >= 0 && row < BOARD_SIZE && col >= 0 && col < BOARD_SIZE && gameBoard[row][col] == ' ') {
            return true;
        }
        return false;
    }
    private boolean isGameOver() {
        // Check for win conditions
        for (int row = 0; row < BOARD_SIZE; row++) {
            if (gameBoard[row][0] != ' ' && gameBoard[row][0] == gameBoard[row][1] && gameBoard[row][0] == gameBoard[row][2]) {
                return true;
            }
        }
        for (int col = 0; col < BOARD_SIZE; col++) {
            if (gameBoard[0][col] != ' ' && gameBoard[0][col] == gameBoard[1][col] && gameBoard[0][col] == gameBoard[2][col]) {
                return true;
            }
        }
        if (gameBoard[0][0] != ' ' && gameBoard[0][0] == gameBoard[1][1] && gameBoard[0][0] == gameBoard[2][2]) {
            return true;
        }
        if (gameBoard[0][2] != ' ' && gameBoard[0][2] == gameBoard[1][1] && gameBoard[0][2] == gameBoard[2][0]) {
            return true;
        }
        return false;
    }
    private boolean isGameDraw() {
        // Check if all positions on the game board are filled
        for (int row = 0; row < BOARD_SIZE; row++) {
            for (int col = 0; col < BOARD_SIZE; col++) {
                if (gameBoard[row][col] == ' ') {
                    return false;
                }
            }
        }
        return true;
    }
    /**
     * This method returns the current game board.
     *
     * @return The current game board.
     */
    public char[][] getGameBoard() {
        return gameBoard;
    }
}