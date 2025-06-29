/**
 * This class represents the income and expense data.
 */
public class IncomeExpenseData {
    private double income;
    private double expense;
    private String category;
    private double savingsTarget;
    public IncomeExpenseData(double income, double expense, String category, double savingsTarget) {
        this.income = income;
        this.expense = expense;
        this.category = category;
        this.savingsTarget = savingsTarget;
    }
    // Getters and setters
    public double getIncome() {
        return income;
    }
    public void setIncome(double income) {
        this.income = income;
    }
    public double getExpense() {
        return expense;
    }
    public void setExpense(double expense) {
        this.expense = expense;
    }
    public String getCategory() {
        return category;
    }
    public void setCategory(String category) {
        this.category = category;
    }
    public double getSavingsTarget() {
        return savingsTarget;
    }
    public void setSavingsTarget(double savingsTarget) {
        this.savingsTarget = savingsTarget;
    }
}