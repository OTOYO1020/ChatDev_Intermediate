'''
This class represents the graphical user interface of the BudgetTrackerLite application.
'''
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class GUI extends JFrame {
    private JTextField incomeField;
    private JTextField expenseField;
    private JButton addButton;
    private JList<String> budgetList;
    private JLabel totalIncomeLabel;
    private JLabel totalExpenseLabel;
    private JLabel remainingBudgetLabel;
    private DefaultListModel<String> budgetListModel;
    private DataManager dataManager;
    public GUI(DataManager dataManager) {
        this.dataManager = dataManager;
        // Set up the GUI components
        incomeField = new JTextField(10);
        expenseField = new JTextField(10);
        addButton = new JButton("Add");
        budgetList = new JList<>();
        budgetListModel = new DefaultListModel<>();
        budgetList.setModel(budgetListModel);
        totalIncomeLabel = new JLabel("Total Income: $0.00");
        totalExpenseLabel = new JLabel("Total Expense: $0.00");
        remainingBudgetLabel = new JLabel("Remaining Budget: $0.00");
        JPanel inputPanel = new JPanel();
        inputPanel.add(new JLabel("Income:"));
        inputPanel.add(incomeField);
        inputPanel.add(new JLabel("Expense:"));
        inputPanel.add(expenseField);
        inputPanel.add(addButton);
        JPanel budgetPanel = new JPanel();
        budgetPanel.setLayout(new BorderLayout());
        budgetPanel.add(new JLabel("Budget List:"), BorderLayout.NORTH);
        budgetPanel.add(new JScrollPane(budgetList), BorderLayout.CENTER);
        JPanel summaryPanel = new JPanel();
        summaryPanel.add(totalIncomeLabel);
        summaryPanel.add(totalExpenseLabel);
        summaryPanel.add(remainingBudgetLabel);
        setLayout(new BorderLayout());
        add(inputPanel, BorderLayout.NORTH);
        add(budgetPanel, BorderLayout.CENTER);
        add(summaryPanel, BorderLayout.SOUTH);
        // Set up event listeners and handle user interactions
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String incomeText = incomeField.getText();
                String expenseText = expenseField.getText();
                if (!incomeText.isEmpty() && !expenseText.isEmpty()) {
                    double income = Double.parseDouble(incomeText);
                    double expense = Double.parseDouble(expenseText);
                    dataManager.addBudgetItem(income, expense);
                    updateBudgetList();
                    updateSummaryLabels();
                    incomeField.setText("");
                    expenseField.setText("");
                }
            }
        });
    }
    public void show() {
        // Display the GUI
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        pack();
        setLocationRelativeTo(null);
        setVisible(true);
    }
    public void updateBudgetList() {
        budgetListModel.clear();
        for (BudgetItem item : dataManager.getBudgetItems()) {
            budgetListModel.addElement(item.toString());
        }
    }
    public void updateSummaryLabels() {
        double totalIncome = dataManager.getTotalIncome();
        double totalExpense = dataManager.getTotalExpense();
        double remainingBudget = totalIncome - totalExpense;
        totalIncomeLabel.setText("Total Income: $" + String.format("%.2f", totalIncome));
        totalExpenseLabel.setText("Total Expense: $" + String.format("%.2f", totalExpense));
        remainingBudgetLabel.setText("Remaining Budget: $" + String.format("%.2f", remainingBudget));
    }
}