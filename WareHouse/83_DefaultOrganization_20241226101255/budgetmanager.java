import java.util.ArrayList;
import java.util.List;
/**
 * This class represents the budget manager that handles budget tracking and management.
 */
public class BudgetManager {
    private List<Double> incomes;
    private List<Double> expenses;
    public BudgetManager() {
        incomes = new ArrayList<>();
        expenses = new ArrayList<>();
    }
    public void addIncome(double amount) {
        incomes.add(amount);
    }
    public void addExpense(double amount) {
        expenses.add(amount);
    }
    public double calculateTotalBudget() {
        double totalIncome = calculateTotalIncome();
        double totalExpense = calculateTotalExpense();
        return totalIncome - totalExpense;
    }
    public void displayBudgetSummary() {
        double totalBudget = calculateTotalBudget();
        System.out.println("Total Budget: $" + totalBudget);
        System.out.println("Incomes: $" + calculateTotalIncome());
        System.out.println("Expenses: $" + calculateTotalExpense());
    }
    private double calculateTotalIncome() {
        double totalIncome = 0;
        for (double income : incomes) {
            totalIncome += income;
        }
        return totalIncome;
    }
    private double calculateTotalExpense() {
        double totalExpense = 0;
        for (double expense : expenses) {
            totalExpense += expense;
        }
        return totalExpense;
    }
}