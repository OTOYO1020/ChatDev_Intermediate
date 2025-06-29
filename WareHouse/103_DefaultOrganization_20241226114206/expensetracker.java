import java.util.ArrayList;
import java.util.List;
import expense.Expense;
/**
 * This class represents the expense tracker and handles the recording and categorization of expenses.
 */
public class ExpenseTracker {
    private List<Expense> expenses;
    public ExpenseTracker() {
        expenses = new ArrayList<>();
    }
    public void addExpense(Expense expense) {
        expenses.add(expense);
    }
    public List<Expense> getExpenses() {
        return expenses;
    }
}