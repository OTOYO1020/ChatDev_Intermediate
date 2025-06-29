import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the graphical user interface of the application.
 */
public class GUI {
    private JFrame frame;
    private JButton button;
    private JTextField incomeField;
    private JTextField expenseField;
    private JTextArea goalsTextArea;
    private JTextArea breakdownTextArea;
    private JTextArea reminderTextArea;
    /**
     * This method starts the GUI and initializes all the necessary components.
     */
    public void start() {
        frame = new JFrame("BudgetTrackerPro");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(800, 600);
        frame.setLayout(new BorderLayout());
        // Create and configure the input panel
        JPanel inputPanel = new JPanel();
        inputPanel.setLayout(new FlowLayout());
        JLabel incomeLabel = new JLabel("Income:");
        incomeField = new JTextField(10);
        inputPanel.add(incomeLabel);
        inputPanel.add(incomeField);
        JLabel expenseLabel = new JLabel("Expense:");
        expenseField = new JTextField(10);
        inputPanel.add(expenseLabel);
        inputPanel.add(expenseField);
        JButton addButton = new JButton("Add");
        addButton.addActionListener(new ButtonClickListener());
        inputPanel.add(addButton);
        frame.add(inputPanel, BorderLayout.NORTH);
        // Create and configure the budget panel
        JPanel budgetPanel = new JPanel();
        budgetPanel.setLayout(new GridLayout(1, 2));
        // Create and configure the goals panel
        JPanel goalsPanel = new JPanel();
        goalsPanel.setLayout(new BorderLayout());
        JLabel goalsLabel = new JLabel("Budget Goals");
        goalsPanel.add(goalsLabel, BorderLayout.NORTH);
        goalsTextArea = new JTextArea();
        goalsPanel.add(goalsTextArea, BorderLayout.CENTER);
        budgetPanel.add(goalsPanel);
        // Create and configure the breakdown panel
        JPanel breakdownPanel = new JPanel();
        breakdownPanel.setLayout(new BorderLayout());
        JLabel breakdownLabel = new JLabel("Budget Breakdown");
        breakdownPanel.add(breakdownLabel, BorderLayout.NORTH);
        breakdownTextArea = new JTextArea();
        breakdownPanel.add(breakdownTextArea, BorderLayout.CENTER);
        budgetPanel.add(breakdownPanel);
        frame.add(budgetPanel, BorderLayout.CENTER);
        // Create and configure the reminder panel
        JPanel reminderPanel = new JPanel();
        reminderPanel.setLayout(new FlowLayout());
        JLabel reminderLabel = new JLabel("Reminders:");
        reminderPanel.add(reminderLabel);
        reminderTextArea = new JTextArea();
        reminderPanel.add(reminderTextArea);
        frame.add(reminderPanel, BorderLayout.SOUTH);
        frame.setVisible(true);
    }
    /**
     * This class represents the action listener for the add button.
     */
    private class ButtonClickListener implements ActionListener {
        public void actionPerformed(ActionEvent event) {
            String income = incomeField.getText();
            String expense = expenseField.getText();
            // Validate and process the income and expense data
            try {
                double incomeAmount = Double.parseDouble(income);
                double expenseAmount = Double.parseDouble(expense);
                // Perform calculations or store the data as needed
                // Update the GUI components with the processed data
                goalsTextArea.setText("Updated goals");
                breakdownTextArea.setText("Updated breakdown");
                reminderTextArea.setText("Updated reminders");
            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(frame, "Invalid input. Please enter numeric values for income and expense.");
            }
        }
    }
}