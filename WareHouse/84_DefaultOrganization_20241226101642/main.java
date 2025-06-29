/**
 * This is the main class that serves as the entry point for the web application.
 * It initializes the GUI and starts the application.
 */
public class Main {
    public static void main(String[] args) {
        // Initialize the GUI
        GUI gui = new GUI();
        // Initialize the BudgetOptimizerPlus class
        BudgetOptimizerPlus budgetOptimizer = new BudgetOptimizerPlus();
        // Start the application
        gui.start();
    }
}