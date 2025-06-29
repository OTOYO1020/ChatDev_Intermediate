import javax.swing.JFrame;
import javax.swing.JOptionPane;
/**
 * This class represents the GUI of the BudgetOptimizerPlus application.
 */
public class GUI {
    private JFrame frame;
    /**
     * Constructor for GUI class.
     */
    public GUI() {
        // Initialize the frame
        frame = new JFrame("BudgetOptimizerPlus");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(800, 600);
        frame.setLocationRelativeTo(null);
    }
    /**
     * Starts the GUI application by making the main window visible.
     */
    public void start() {
        // Show the main window
        frame.setVisible(true);
    }
    /**
     * Displays a message dialog with the given message.
     *
     * @param message The message to be displayed
     */
    private void showMessage(String message) {
        // Show a message dialog
        JOptionPane.showMessageDialog(frame, message);
    }
}