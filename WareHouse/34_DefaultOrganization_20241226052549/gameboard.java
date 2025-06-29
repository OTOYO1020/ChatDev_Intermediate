/**
 * This class represents the game board for the tile placement game.
 * It handles the initialization of the board, tile placement, and point calculation.
 */
public class GameBoard {
    private int[][] board;
    private List<Tile> availableTiles;
    private List<Player> players;
    private int currentPlayerIndex;
    public GameBoard() {
        // Initialize the board with empty spaces
        board = new int[8][8];
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                board[i][j] = 0;
            }
        }
        // Initialize the available tiles
        availableTiles = new ArrayList<>();
        availableTiles.add(new Tile(1, "Red"));
        availableTiles.add(new Tile(2, "Blue"));
        availableTiles.add(new Tile(3, "Green"));
        availableTiles.add(new Tile(4, "Yellow"));
        // Initialize the players
        players = new ArrayList<>();
        players.add(new Player("Player 1"));
        players.add(new Player("Player 2"));
        // Set the current player index to 0
        currentPlayerIndex = 0;
    }
    public int[][] getBoard() {
        return board;
    }
    public List<Tile> getAvailableTiles() {
        return availableTiles;
    }
    public List<Player> getPlayers() {
        return players;
    }
    public int getCurrentPlayerIndex() {
        return currentPlayerIndex;
    }
    public void placeTile(int row, int col, Tile tile) {
        // Check if the tile can be placed at the specified position
        if (isValidPlacement(row, col, tile)) {
            // Place the tile on the board
            board[row][col] = tile.getId();
            // Calculate the points for the current player
            int points = calculatePoints(row, col);
            players.get(currentPlayerIndex).addPoints(points);
            // Update the current player index
            currentPlayerIndex = (currentPlayerIndex + 1) % players.size();
        }
    }
    private boolean isValidPlacement(int row, int col, Tile tile) {
        // Check if the position is within the board bounds
        if (row < 0 || row >= 8 || col < 0 || col >= 8) {
            return false;
        }
        // Check if the position is empty
        if (board[row][col] != 0) {
            return false;
        }
        // Check if the tile is available
        if (!availableTiles.contains(tile)) {
            return false;
        }
        return true;
    }
    private int calculatePoints(int row, int col) {
        int points = 0;
        // Check for horizontal combinations
        int horizontalCount = 1;
        for (int i = col - 1; i >= 0; i--) {
            if (board[row][i] == board[row][col]) {
                horizontalCount++;
            } else {
                break;
            }
        }
        for (int i = col + 1; i < 8; i++) {
            if (board[row][i] == board[row][col]) {
                horizontalCount++;
            } else {
                break;
            }
        }
        if (horizontalCount >= 3) {
            points += horizontalCount;
        }
        // Check for vertical combinations
        int verticalCount = 1;
        for (int i = row - 1; i >= 0; i--) {
            if (board[i][col] == board[row][col]) {
                verticalCount++;
            } else {
                break;
            }
        }
        for (int i = row + 1; i < 8; i++) {
            if (board[i][col] == board[row][col]) {
                verticalCount++;
            } else {
                break;
            }
        }
        if (verticalCount >= 3) {
            points += verticalCount;
        }
        return points;
    }
}