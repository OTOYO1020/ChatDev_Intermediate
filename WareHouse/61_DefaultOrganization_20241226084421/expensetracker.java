import java.util.ArrayList;
import java.util.List;
/**
 * This class represents the expense tracker that keeps track of expenses.
 */
public class ExpenseTracker {
    private List<Double> expenses;
    public ExpenseTracker() {
        expenses = new ArrayList<>();
    }
    public void addExpense(double amount) {
        expenses.add(amount);
    }
    public double getTotalExpenses() {
        double total = 0.0;
        for (double expense : expenses) {
            total += expense;
        }
        return total;
    }
}