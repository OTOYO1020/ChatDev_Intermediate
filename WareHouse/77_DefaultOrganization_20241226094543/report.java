import java.util.*;
/**
 * This class represents the report generation in the SavingsTracker application.
 */
public class Report {
    private List<Double> incomes;
    private List<Double> expenses;
    private double savingsTarget;
    public Report(List<Double> incomes, List<Double> expenses, double savingsTarget) {
        this.incomes = incomes;
        this.expenses = expenses;
        this.savingsTarget = savingsTarget;
    }
    /**
     * Generate a report based on the income, expenses, and savings target.
     * @return The generated report.
     */
    public String generateReport() {
        StringBuilder report = new StringBuilder();
        report.append("Income:\n");
        for (double income : incomes) {
            report.append(income).append("\n");
        }
        report.append("\nExpenses:\n");
        for (double expense : expenses) {
            report.append(expense).append("\n");
        }
        report.append("\nSavings Target: ").append(savingsTarget).append("\n");
        double totalIncome = calculateTotalIncome();
        double totalExpenses = calculateTotalExpenses();
        double savings = totalIncome - totalExpenses;
        report.append("\nTotal Income: ").append(totalIncome).append("\n");
        report.append("Total Expenses: ").append(totalExpenses).append("\n");
        report.append("Savings: ").append(savings).append("\n");
        if (savingsTarget > 0) {
            boolean targetAchieved = savingsTarget <= savings;
            report.append("Savings Target Achieved: ").append(targetAchieved).append("\n");
        }
        return report.toString();
    }
    /**
     * Calculate the total income.
     * @return The total income.
     */
    private double calculateTotalIncome() {
        return incomes.stream().mapToDouble(Double::doubleValue).sum();
    }
    /**
     * Calculate the total expenses.
     * @return The total expenses.
     */
    private double calculateTotalExpenses() {
        return expenses.stream().mapToDouble(Double::doubleValue).sum();
    }
}