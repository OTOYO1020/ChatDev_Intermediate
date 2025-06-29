/**
 * This class represents a report with financial analysis details.
 */
import java.util.List;
public class Report {
    private double totalExpenses;
    private double totalBudgets;
    private double remainingBudget;
    private List<Budget> budgets;
    public Report(double totalExpenses, double totalBudgets, double remainingBudget, List<Budget> budgets) {
        this.totalExpenses = totalExpenses;
        this.totalBudgets = totalBudgets;
        this.remainingBudget = remainingBudget;
        this.budgets = budgets;
    }
    public double getTotalExpenses() {
        return totalExpenses;
    }
    public double getTotalBudgets() {
        return totalBudgets;
    }
    public double getRemainingBudget() {
        return remainingBudget;
    }
    public List<Budget> getBudgets() {
        return budgets;
    }
}