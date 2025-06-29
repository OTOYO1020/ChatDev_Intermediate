/**
 * This class manages the budgets and provides methods to retrieve and manipulate them.
 */
import java.util.ArrayList;
import java.util.List;
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