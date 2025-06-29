/**
 * This is the main class that contains the entry point of the application.
 */
public class Main {
    public static void main(String[] args) {
        // Create an instance of the ExpenseTracker class
        ExpenseTracker expenseTracker = new ExpenseTracker();
        // Create an instance of the GUI class and pass the expenseTracker reference
        GUI gui = new GUI(expenseTracker);
        // Start the GUI
        gui.start();
    }
}