import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class GUI extends JFrame {
    private JTextField incomeField;
    private JTextField expenseField;
    private BudgetAssistant budgetAssistant;
    public GUI(BudgetAssistant budgetAssistant) {
        this.budgetAssistant = budgetAssistant;
        setTitle("Budget Assistant");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());
        // Create and add GUI components
        JLabel incomeLabel = new JLabel("Income:");
        add(incomeLabel);
        incomeField = new JTextField(10);
        add(incomeField);
        JLabel expenseLabel = new JLabel("Expense:");
        add(expenseLabel);
        expenseField = new JTextField(10);
        add(expenseField);
        JButton analyzeButton = new JButton("Analyze");
        analyzeButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                analyzeBudget();
            }
        });
        add(analyzeButton);
        pack();
        setVisible(true);
    }
    private void analyzeBudget() {
        double income = Double.parseDouble(incomeField.getText());
        double expenses = Double.parseDouble(expenseField.getText());
        double savings = budgetAssistant.analyzeBudget(income, expenses);
        JOptionPane.showMessageDialog(this, "Your savings: $" + savings);
    }
}