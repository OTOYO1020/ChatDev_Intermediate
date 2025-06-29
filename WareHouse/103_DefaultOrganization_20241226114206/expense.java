package expense;
/**
 * This class represents an expense and contains properties such as amount, category, and date.
 */
public class Expense {
    private String expense;
    private String category;
    private double budgetLimit;
    public Expense(String expense, String category, double budgetLimit) {
        this.expense = expense;
        this.category = category;
        this.budgetLimit = budgetLimit;
    }
    public String getExpense() {
        return expense;
    }
    public String getCategory() {
        return category;
    }
    public double getBudgetLimit() {
        return budgetLimit;
    }
}