/**
 * This class represents a dialog for adding an expense.
 */
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class AddExpenseDialog extends JDialog {
    private JTextField categoryField;
    private JTextField amountField;
    private JButton confirmButton;
    private JButton cancelButton;
    private boolean confirmed;
    private Expense expense;
    public AddExpenseDialog(Frame owner) {
        super(owner, "Add Expense", true);
        setSize(300, 200);
        setLayout(new GridLayout(3, 2));
        JLabel categoryLabel = new JLabel("Category:");
        categoryField = new JTextField();
        JLabel amountLabel = new JLabel("Amount:");
        amountField = new JTextField();
        confirmButton = new JButton("Confirm");
        confirmButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String category = categoryField.getText();
                double amount = Double.parseDouble(amountField.getText());
                expense = new Expense(category, amount);
                confirmed = true;
                dispose();
            }
        });
        cancelButton = new JButton("Cancel");
        cancelButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                confirmed = false;
                dispose();
            }
        });
        add(categoryLabel);
        add(categoryField);
        add(amountLabel);
        add(amountField);
        add(confirmButton);
        add(cancelButton);
    }
    public boolean isConfirmed() {
        return confirmed;
    }
    public Expense getExpense() {
        return expense;
    }
}