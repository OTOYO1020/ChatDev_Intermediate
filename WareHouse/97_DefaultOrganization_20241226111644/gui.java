import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import com.example.Model;
/**
 * This class represents the graphical user interface of the web application.
 */
public class GUI extends JFrame {
    private JTextField expenseField;
    private JComboBox<String> categoryComboBox;
    private JButton addButton;
    private JTextArea expenseListArea;
    private Model model;
    public GUI(Model model) {
        this.model = model;
        // Create and configure the GUI components
        expenseField = new JTextField();
        categoryComboBox = new JComboBox<>(new String[]{"Category 1", "Category 2", "Category 3"});
        addButton = new JButton("Add Expense");
        expenseListArea = new JTextArea();
        // Set layout manager for the JFrame
        setLayout(new BorderLayout());
        // Create a JPanel for the input fields and button
        JPanel inputPanel = new JPanel();
        inputPanel.setLayout(new FlowLayout());
        inputPanel.add(new JLabel("Expense:"));
        inputPanel.add(expenseField);
        inputPanel.add(new JLabel("Category:"));
        inputPanel.add(categoryComboBox);
        inputPanel.add(addButton);
        // Add the input panel to the JFrame
        add(inputPanel, BorderLayout.NORTH);
        // Add the expense list area to the JFrame
        add(new JScrollPane(expenseListArea), BorderLayout.CENTER);
        // Configure the JFrame
        setTitle("Business Expense Tracker");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        pack();
        setLocationRelativeTo(null);
        // Add event listener for the add button
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String expense = expenseField.getText();
                String category = (String) categoryComboBox.getSelectedItem();
                // Add the expense to the model
                model.addExpense(expense, category);
                // Update the expense list area
                expenseListArea.setText(model.getExpenseList());
                // Clear the expense field
                expenseField.setText("");
            }
        });
    }
}