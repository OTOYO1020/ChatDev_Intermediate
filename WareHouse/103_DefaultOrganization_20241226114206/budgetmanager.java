import java.util.ArrayList;
import java.util.List;
import budget.Budget;
/**
 * This class represents the budget manager and handles the management of predefined budgets.
 */
public class BudgetManager {
    private List<Budget> budgets;
    public BudgetManager() {
        budgets = new ArrayList<>();
    }
    public void addBudget(Budget budget) {
        budgets.add(budget);
    }
    public List<Budget> getBudgets() {
        return budgets;
    }
}