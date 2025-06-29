/**
 * This class manages the expenses and provides methods to retrieve and manipulate them.
 */
import java.util.ArrayList;
import java.util.List;
public class ExpenseManager {
    private List<Expense> expenses;
    public ExpenseManager() {
        expenses = new ArrayList<>();
    }
    public void addExpense(Expense expense) {
        expenses.add(expense);
    }
    public List<Expense> getExpenses() {
        return expenses;
    }
}