package GUI;
import java.util.*;
public class BudgetManager {
    private double income;
    private double expense;
    private double savingsGoal;
    public BudgetManager(double income, double expense, double savingsGoal) {
        this.income = income;
        this.expense = expense;
        this.savingsGoal = savingsGoal;
    }
    public double calculateSavings() {
        return income - expense;
    }
    public double calculatePercentage() {
        return (calculateSavings() / income) * 100;
    }
    public String getBudgetBreakdown() {
        double savings = calculateSavings();
        double percentage = calculatePercentage();
        String breakdown = "Savings: $" + savings + " (" + percentage + "%)";
        if (savings >= savingsGoal) {
            breakdown += " - Goal Achieved!";
        } else {
            double remaining = savingsGoal - savings;
            breakdown += " - Remaining: $" + remaining;
        }
        return breakdown;
    }
}