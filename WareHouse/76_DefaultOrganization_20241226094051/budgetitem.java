'''
This class represents a budget item with income and expense values.
'''
public class BudgetItem {
    private double income;
    private double expense;
    public BudgetItem(double income, double expense) {
        this.income = income;
        this.expense = expense;
    }
    public double getIncome() {
        return income;
    }
    public double getExpense() {
        return expense;
    }
    @Override
    public String toString() {
        return "Income: $" + String.format("%.2f", income) + ", Expense: $" + String.format("%.2f", expense);
    }
}