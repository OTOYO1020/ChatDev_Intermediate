/**
 * This is the main class that serves as the entry point for the application.
 * It initializes the BudgetMonitor class and starts the application.
 */
import javax.swing.*;
public class Main {
    public static void main(String[] args) {
        // Create an instance of the GUI class
        GUI gui = new GUI();
        // Create an instance of the BudgetMonitor class and pass the GUI instance
        BudgetMonitor budgetMonitor = new BudgetMonitor(gui);
        // Start the application
        SwingUtilities.invokeLater(budgetMonitor::start);
    }
}