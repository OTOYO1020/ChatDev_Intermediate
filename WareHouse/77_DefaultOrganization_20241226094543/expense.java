import java.util.*;
/**
 * This class represents the expense-related operations in the SavingsTracker application.
 */
public class Expense {
    private List<Double> expenses;
    public Expense() {
        expenses = new ArrayList<>();
    }
    /**
     * Add expense amount to the list of expenses.
     * @param amount The expense amount to be added.
     */
    public void addExpense(double amount) {
        expenses.add(amount);
    }
    /**
     * Calculate the total expenses.
     * @return The total expenses.
     */
    public double calculateTotalExpenses() {
        return expenses.stream().mapToDouble(Double::doubleValue).sum();
    }
    /**
     * Get the list of expenses.
     * @return The list of expenses.
     */
    public List<Double> getExpenses() {
        return expenses;
    }
}