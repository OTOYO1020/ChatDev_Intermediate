/**
 * This is the main class that serves as the entry point of the BudgetAdvisor application.
 */
import javax.swing.SwingUtilities;
public class Main {
    public static void main(String[] args) {
        // Create an instance of the GUI class
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                GUI guiInstance = new GUI();
                guiInstance.createAndShowGUI();
            }
        });
    }
}