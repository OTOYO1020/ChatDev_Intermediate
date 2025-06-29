/**
 * This is the main class of the web application.
 * It initializes the GUI and handles user interactions.
 */
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class Main {
    public static void main(String[] args) {
        // Create instances of ExpenseManager, BudgetManager, and ReportGenerator
        ExpenseManager expenseManager = new ExpenseManager();
        BudgetManager budgetManager = new BudgetManager();
        ReportGenerator reportGenerator = new ReportGenerator();
        // Initialize the GUI and set the ExpenseManager, BudgetManager, and ReportGenerator
        GUI gui = new GUI();
        gui.setExpenseManager(expenseManager);
        gui.setBudgetManager(budgetManager);
        gui.setReportGenerator(reportGenerator);
        gui.initialize();
    }
}