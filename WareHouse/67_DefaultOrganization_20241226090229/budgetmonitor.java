import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the BudgetMonitor application.
 * It provides functionality to track and monitor the budget.
 */
public class BudgetMonitor {
    private GUI gui;
    private JButton addButton;
    private JButton generateReportButton;
    private JLabel incomeLabel;
    private JLabel expenseLabel;
    private JLabel totalLabel;
    private double income;
    private double expenses;
    private double total;
    public BudgetMonitor(GUI gui) {
        this.gui = gui; // Use the existing instance of the GUI class
        // Create buttons
        addButton = new JButton("Add Transaction");
        generateReportButton = new JButton("Generate Report");
        // Create labels
        incomeLabel = new JLabel("Income: $0.00");
        expenseLabel = new JLabel("Expenses: $0.00");
        totalLabel = new JLabel("Total: $0.00");
        // Add action listeners to buttons
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Open a dialog to add a new transaction
                String input = JOptionPane.showInputDialog(gui.getFrame(), "Enter transaction amount:");
                if (input != null && !input.isEmpty()) {
                    double amount = Double.parseDouble(input);
                    if (amount > 0) {
                        income += amount;
                        total += amount;
                        updateLabels();
                    } else if (amount < 0) {
                        expenses -= amount;
                        total += amount;
                        updateLabels();
                    }
                }
            }
        });
        generateReportButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Generate and display a report
                String report = "Income: $" + income + "\n" +
                        "Expenses: $" + expenses + "\n" +
                        "Total: $" + total;
                JOptionPane.showMessageDialog(gui.getFrame(), report, "Budget Report", JOptionPane.INFORMATION_MESSAGE);
            }
        });
    }
    public void start() {
        // Add buttons and labels to the frame
        gui.getFrame().add(addButton);
        gui.getFrame().add(generateReportButton);
        gui.getFrame().add(incomeLabel);
        gui.getFrame().add(expenseLabel);
        gui.getFrame().add(totalLabel);
        // Make the frame visible
        gui.getFrame().setVisible(true);
    }
    private void updateLabels() {
        incomeLabel.setText("Income: $" + income);
        expenseLabel.setText("Expenses: $" + expenses);
        totalLabel.setText("Total: $" + total);
    }
}