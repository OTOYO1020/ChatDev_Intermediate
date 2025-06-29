import java.util.List;
import java.util.ArrayList;
/**
 * This class represents the game analyzer that analyzes board game strategies based on historical game data.
 */
public class GameAnalyzer {
    private List<Strategy> strategies;
    private GUI gui;
    public GameAnalyzer() {
        // Initialize the list of strategies
        strategies = StrategyData.getStrategies();
    }
    /**
     * This method starts the game analyzer.
     */
    public void start() {
        // Create an instance of the GUI class and pass the game analyzer instance
        gui = new GUI(this);
        // Start the GUI
        gui.setVisible(true);
    }
    /**
     * This method analyzes the board game strategies and provides statistical insights and recommendations to players.
     */
    public void analyze() {
        // Clear the text area before displaying the analysis results
        gui.getTextArea().setText("");
        // Perform analysis on the strategies
        for (Strategy strategy : strategies) {
            // Calculate the success rate for each strategy
            double successRate = strategy.getSuccessRate();
            // Append the strategy name and success rate to the text area
            gui.getTextArea().append("Strategy: " + strategy.getName() + "\n");
            gui.getTextArea().append("Success Rate: " + successRate + "\n");
            gui.getTextArea().append("---------------------------\n");
        }
    }
}