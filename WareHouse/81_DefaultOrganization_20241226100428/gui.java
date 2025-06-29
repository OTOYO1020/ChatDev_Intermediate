import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the graphical user interface (GUI) of the application.
 * It contains the main window and handles user interactions.
 */
public class GUI {
    private JFrame frame;
    private JButton button;
    private JLabel label;
    private JTextField incomeField;
    private JTextField expenseField;
    public GUI() {
        // Create the main window
        frame = new JFrame("BudgetPro");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        // Create the label
        label = new JLabel("Hello, world!");
        // Create the button
        button = new JButton("Click me");
        button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Handle button click event
                label.setText("Button clicked");
            }
        });
        // Create the income input field
        incomeField = new JTextField(10);
        // Create the expense input field
        expenseField = new JTextField(10);
    }
    /**
     * This method adds the components to the frame, centers the frame on the screen,
     * and makes the frame visible.
     */
    public void start() {
        // Add components to the frame
        frame.setLayout(new FlowLayout());
        frame.add(new JLabel("Income:"));
        frame.add(incomeField);
        frame.add(new JLabel("Expense:"));
        frame.add(expenseField);
        frame.add(button);
        frame.add(label);
        // Center the frame on the screen
        frame.setLocationRelativeTo(null);
        // Make the frame visible
        frame.setVisible(true);
    }
}