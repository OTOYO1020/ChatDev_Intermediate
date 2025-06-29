/**
 * This class generates reports for financial analysis.
 */
import java.util.List;
public class ReportGenerator {
    public Report generateReport(ExpenseManager expenseManager, BudgetManager budgetManager) {
        double totalExpenses = calculateTotalExpenses(expenseManager);
        double totalBudgets = calculateTotalBudgets(budgetManager);
        double remainingBudget = calculateRemainingBudget(totalBudgets, totalExpenses);
        List<Budget> budgets = budgetManager.getBudgets();
        return new Report(totalExpenses, totalBudgets, remainingBudget, budgets);
    }
    private double calculateTotalExpenses(ExpenseManager expenseManager) {
        double totalExpenses = 0;
        List<Expense> expenses = expenseManager.getExpenses();
        for (Expense expense : expenses) {
            totalExpenses += expense.getAmount();
        }
        return totalExpenses;
    }
    private double calculateTotalBudgets(BudgetManager budgetManager) {
        double totalBudgets = 0;
        List<Budget> budgets = budgetManager.getBudgets();
        for (Budget budget : budgets) {
            totalBudgets += budget.getLimit();
        }
        return totalBudgets;
    }
    private double calculateRemainingBudget(double totalBudgets, double totalExpenses) {
        return totalBudgets - totalExpenses;
    }
}