/**
 * This class represents the graphical user interface (GUI) for the application.
 * It contains the main window and handles user interactions.
 */
public class GUI {
    private JFrame frame;
    private JButton[][] buttons;
    private JLabel[] playerLabels;
    private GameBoard gameBoard;
    private int selectedTileIndex = -1; // Initialize selectedTileIndex to -1
    public GUI(GameBoard gameBoard) {
        this.gameBoard = gameBoard;
        // Create the main window
        frame = new JFrame("Tile Placement Game");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);
        // Create the game board buttons
        buttons = new JButton[8][8];
        JPanel boardPanel = new JPanel(new GridLayout(8, 8));
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                buttons[i][j] = new JButton();
                buttons[i][j].addActionListener(new TilePlacementListener(i, j));
                boardPanel.add(buttons[i][j]);
            }
        }
        // Create the player labels
        List<Player> players = gameBoard.getPlayers();
        playerLabels = new JLabel[players.size()];
        JPanel playerPanel = new JPanel(new GridLayout(players.size(), 1));
        for (int i = 0; i < players.size(); i++) {
            playerLabels[i] = new JLabel(players.get(i).getName() + ": 0 points");
            playerPanel.add(playerLabels[i]);
        }
        // Add the game board and player panels to the main window
        frame.getContentPane().setLayout(new BorderLayout());
        frame.getContentPane().add(boardPanel, BorderLayout.CENTER);
        frame.getContentPane().add(playerPanel, BorderLayout.EAST);
    }
    public void start() {
        // Display the main window
        frame.setVisible(true);
    }
    public void setSelectedTileIndex(int index) {
        selectedTileIndex = index;
    }
    private class TilePlacementListener implements ActionListener {
        private int row;
        private int col;
        public TilePlacementListener(int row, int col) {
            this.row = row;
            this.col = col;
        }
        public void actionPerformed(ActionEvent e) {
            // Get the current player and selected tile
            List<Player> players = gameBoard.getPlayers();
            Player currentPlayer = players.get(gameBoard.getCurrentPlayerIndex());
            List<Tile> availableTiles = gameBoard.getAvailableTiles();
            // Check if selectedTileIndex is within valid range
            if (selectedTileIndex >= 0 && selectedTileIndex < availableTiles.size()) {
                Tile selectedTile = availableTiles.get(selectedTileIndex);
                // Place the tile on the game board
                gameBoard.placeTile(row, col, selectedTile);
                // Update the button text and player label
                buttons[row][col].setText(selectedTile.getColor());
                playerLabels[gameBoard.getCurrentPlayerIndex()].setText(currentPlayer.getName() + ": " + currentPlayer.getPoints() + " points");
            }
        }
    }
}