import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the GUI of the SavingsTracker application.
 */
public class GUI extends JFrame implements ActionListener {
    private JTextField incomeTextField;
    private JTextField expenseTextField;
    private JTextField savingsTargetTextField;
    private JButton addButton;
    private JButton generateReportButton;
    private Income income;
    private Expense expense;
    private SavingsTarget savingsTarget;
    private Report report;
    /**
     * Constructor to initialize the GUI components.
     */
    public GUI() {
        setTitle("SavingsTracker");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridLayout(4, 2));
        JLabel incomeLabel = new JLabel("Income:");
        incomeTextField = new JTextField();
        JLabel expenseLabel = new JLabel("Expense:");
        expenseTextField = new JTextField();
        JLabel savingsTargetLabel = new JLabel("Savings Target:");
        savingsTargetTextField = new JTextField();
        addButton = new JButton("Add");
        addButton.addActionListener(this);
        generateReportButton = new JButton("Generate Report");
        generateReportButton.addActionListener(this);
        add(incomeLabel);
        add(incomeTextField);
        add(expenseLabel);
        add(expenseTextField);
        add(savingsTargetLabel);
        add(savingsTargetTextField);
        add(addButton);
        add(generateReportButton);
        pack();
        setLocationRelativeTo(null);
        income = new Income();
        expense = new Expense();
    }
    /**
     * Method to start the GUI application.
     */
    public void start() {
        setVisible(true);
    }
    /**
     * ActionListener implementation to handle button clicks.
     */
    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == addButton) {
            handleAddButtonClick();
        } else if (e.getSource() == generateReportButton) {
            handleGenerateReportButtonClick();
        }
    }
    /**
     * Handle add button click.
     */
    private void handleAddButtonClick() {
        String incomeInput = incomeTextField.getText();
        String expenseInput = expenseTextField.getText();
        // Validate input
        if (incomeInput.isEmpty() || expenseInput.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Please enter income and expense amounts", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }
        // Parse input
        double incomeAmount;
        double expenseAmount;
        try {
            incomeAmount = Double.parseDouble(incomeInput);
            expenseAmount = Double.parseDouble(expenseInput);
        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this, "Invalid input", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }
        // Add income and expense amounts
        income.addIncome(incomeAmount);
        expense.addExpense(expenseAmount);
        // Clear input fields
        incomeTextField.setText("");
        expenseTextField.setText("");
    }
    /**
     * Handle generate report button click.
     */
    private void handleGenerateReportButtonClick() {
        String savingsTargetInput = savingsTargetTextField.getText();
        // Validate input
        if (savingsTargetInput.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Please enter a savings target amount", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }
        // Parse input
        double savingsTargetAmount;
        try {
            savingsTargetAmount = Double.parseDouble(savingsTargetInput);
        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this, "Invalid input", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }
        // Update savings target
        savingsTarget = new SavingsTarget(savingsTargetAmount);
        // Generate report
        report = new Report(income.getIncomes(), expense.getExpenses(), savingsTargetAmount);
        String generatedReport = report.generateReport();
        // Display report
        JOptionPane.showMessageDialog(this, generatedReport, "Report", JOptionPane.INFORMATION_MESSAGE);
        // Clear input field
        savingsTargetTextField.setText("");
    }
}