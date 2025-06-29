/**
 * This class represents the solver algorithm.
 * It calculates the best possible moves for each player, considering both short-term gains and long-term strategies.
 */
public class Solver {
    private GUI gui;
    public Solver(GUI gui) {
        this.gui = gui;
    }
    public void calculateMoves(Board board, Player[] players) {
        // Call the analyzeState() method of the board to update the current state
        board.analyzeState();
        // Call the calculateMoves() method of the board to calculate the best moves
        board.calculateMoves();
        // Display the game board and highlight the best moves for each player using the GUI class
        gui.displayBoard(board);
        gui.highlightMoves(board, players);
        // Provide textual instructions on what actions to take using the GUI class
        gui.displayInstructions(board, players);
        // Call the performAction() method of each player to perform the calculated moves
        for (Player player : players) {
            player.performAction();
        }
        // Call the updateResources() method of each player to update their resources
        for (Player player : players) {
            player.updateResources();
        }
    }
}