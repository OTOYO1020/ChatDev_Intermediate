/**
 * This class contains the main method to start the BudgetTracker application.
 */
public class main {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                gui.createAndShowGUI();
            }
        });
    }
}