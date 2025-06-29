import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JLabel;
/**
 * This class represents the GUI of the BudgetAdvisor application.
 */
public class GUI {
    public void createAndShowGUI() {
        // Create and configure the main frame
        JFrame frame = new JFrame("BudgetAdvisor");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        // Create a panel to hold the content
        JPanel panel = new JPanel();
        // Add a label to display personalized financial advice and guidance
        JLabel adviceLabel = new JLabel("Welcome to BudgetAdvisor! Here's your personalized financial advice.");
        panel.add(adviceLabel);
        // Add the panel to the frame
        frame.getContentPane().add(panel);
        // Display the frame
        frame.setVisible(true);
    }
}