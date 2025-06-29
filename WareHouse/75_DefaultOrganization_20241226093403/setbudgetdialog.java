/**
 * This class represents a dialog for setting a budget.
 */
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class SetBudgetDialog extends JDialog {
    private JTextField categoryField;
    private JTextField limitField;
    private JButton confirmButton;
    private JButton cancelButton;
    private boolean confirmed;
    private Budget budget;
    public SetBudgetDialog(Frame owner) {
        super(owner, "Set Budget", true);
        setSize(300, 200);
        setLayout(new GridLayout(3, 2));
        JLabel categoryLabel = new JLabel("Category:");
        categoryField = new JTextField();
        JLabel limitLabel = new JLabel("Limit:");
        limitField = new JTextField();
        confirmButton = new JButton("Confirm");
        confirmButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String category = categoryField.getText();
                double limit = Double.parseDouble(limitField.getText());
                budget = new Budget(category, limit);
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
        add(limitLabel);
        add(limitField);
        add(confirmButton);
        add(cancelButton);
    }
    public boolean isConfirmed() {
        return confirmed;
    }
    public Budget getBudget() {
        return budget;
    }
}