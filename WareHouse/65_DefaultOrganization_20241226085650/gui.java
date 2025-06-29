import javax.swing.DefaultListModel;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JButton;
import javax.swing.JList;
import javax.swing.JOptionPane;
import javax.swing.JScrollPane;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the graphical user interface of the BudgetTracker application.
 */
public class gui implements ActionListener {
    private static DefaultListModel<String> expenseListModel;
    private static JList<String> expenseList;
    public void actionPerformed(ActionEvent e) {
        String command = e.getActionCommand();
        if (command.equals("addExpense")) {
            String expense = JOptionPane.showInputDialog("Enter expense:");
            expenseListModel.addElement(expense);
        } else if (command.equals("deleteExpense")) {
            int selectedIndex = expenseList.getSelectedIndex();
            if (selectedIndex != -1) {
                expenseListModel.remove(selectedIndex);
            }
        } else if (command.equals("editExpense")) {
            int selectedIndex = expenseList.getSelectedIndex();
            if (selectedIndex != -1) {
                String expense = JOptionPane.showInputDialog("Enter modified expense:");
                expenseListModel.set(selectedIndex, expense);
            }
        }
    }
    public static void createAndShowGUI() {
        JFrame frame = new JFrame("Budget Tracker");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        JPanel panel = new JPanel();
        JButton addExpenseButton = new JButton("Add Expense");
        addExpenseButton.setActionCommand("addExpense");
        addExpenseButton.addActionListener(new gui());
        panel.add(addExpenseButton);
        JButton deleteExpenseButton = new JButton("Delete Expense");
        deleteExpenseButton.setActionCommand("deleteExpense");
        deleteExpenseButton.addActionListener(new gui());
        panel.add(deleteExpenseButton);
        JButton editExpenseButton = new JButton("Edit Expense");
        editExpenseButton.setActionCommand("editExpense");
        editExpenseButton.addActionListener(new gui());
        panel.add(editExpenseButton);
        expenseListModel = new DefaultListModel<>();
        expenseList = new JList<>(expenseListModel);
        JScrollPane scrollPane = new JScrollPane(expenseList);
        panel.add(scrollPane);
        frame.getContentPane().add(panel);
        frame.pack();
        frame.setVisible(true);
    }
}