import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.SwingUtilities;
/**
 * This class represents the GUI of the Profit Margin Analyzer application.
 * It provides a user interface for inputting sales revenue and cost data,
 * calculating profit margins, and displaying reports and visualizations.
 */
public class GUI {
    // GUI components
    private JFrame frame;
    private JLabel revenueLabel;
    private JLabel costLabel;
    private JButton calculateButton;
    /**
     * Constructor to initialize the GUI components.
     */
    public GUI() {
        // Create the main frame
        frame = new JFrame("Profit Margin Analyzer");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        frame.setLayout(null);
        // Create the revenue label
        revenueLabel = new JLabel("Sales Revenue:");
        revenueLabel.setBounds(50, 50, 100, 30);
        frame.add(revenueLabel);
        // Create the cost label
        costLabel = new JLabel("Cost:");
        costLabel.setBounds(50, 100, 100, 30);
        frame.add(costLabel);
        // Create the calculate button
        calculateButton = new JButton("Calculate");
        calculateButton.setBounds(150, 150, 100, 30);
        calculateButton.addActionListener(e -> calculateProfitMargin());
        frame.add(calculateButton);
    }
    /**
     * Method to start the GUI application.
     */
    public void start() {
        frame.setVisible(true);
    }
    /**
     * Method to calculate the profit margin based on the input data.
     */
    private void calculateProfitMargin() {
        // Get the sales revenue and cost values from the user input
        String revenueStr = JOptionPane.showInputDialog(frame, "Enter Sales Revenue:");
        String costStr = JOptionPane.showInputDialog(frame, "Enter Cost:");
        // Parse the input values to double
        double revenue = Double.parseDouble(revenueStr);
        double cost = Double.parseDouble(costStr);
        // Calculate the profit margin
        double profitMargin = (revenue - cost) / revenue * 100;
        // Display the profit margin
        JOptionPane.showMessageDialog(frame, "Profit Margin: " + profitMargin + "%");
    }
}