import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;
/**
 * This class represents the GUI for the BudgetOptimizerLite application.
 * It provides a user-friendly interface for users to input their income and expenses.
 */
public class GUI {
    private JFrame frame;
    private JLabel incomeLabel;
    private JTextField incomeTextField;
    private JLabel expenseLabel;
    private JTextField expenseTextField;
    private JButton calculateButton;
    /**
     * This method starts the GUI application.
     * It creates the frame, initializes the components, and sets up event listeners.
     */
    public void start() {
        // Create the frame
        frame = new JFrame("Budget Optimizer Lite");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new GridLayout(3, 2));
        // Create the income label and text field
        incomeLabel = new JLabel("Income:");
        incomeTextField = new JTextField();
        frame.add(incomeLabel);
        frame.add(incomeTextField);
        // Create the expense label and text field
        expenseLabel = new JLabel("Expense:");
        expenseTextField = new JTextField();
        frame.add(expenseLabel);
        frame.add(expenseTextField);
        // Create the calculate button
        calculateButton = new JButton("Calculate");
        calculateButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Perform the budget calculation
                double income = Double.parseDouble(incomeTextField.getText());
                double expense = Double.parseDouble(expenseTextField.getText());
                double budget = income - expense;
                // Display the budget breakdown
                System.out.println("Income: " + income);
                System.out.println("Expense: " + expense);
                System.out.println("Budget: " + budget);
            }
        });
        frame.add(calculateButton);
        // Set the frame size and make it visible
        frame.pack();
        frame.setVisible(true);
    }
}