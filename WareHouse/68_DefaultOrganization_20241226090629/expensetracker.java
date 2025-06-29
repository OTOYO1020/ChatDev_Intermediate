import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
/**
 * This class represents an expense tracker that tracks and categorizes expenses.
 */
public class ExpenseTracker {
    private List<Expense> expenses;
    private List<ExpenseCategory> categories;
    public ExpenseTracker() {
        expenses = new ArrayList<>();
        categories = new ArrayList<>();
    }
    public void addExpense(String expense, String category) {
        // Create a new Expense object and add it to the expenses list
        Expense newExpense = new Expense(0.0, category, "");
        expenses.add(newExpense);
        // Check if the category already exists in the categories list
        boolean categoryExists = false;
        for (ExpenseCategory expenseCategory : categories) {
            if (expenseCategory.getName().equals(category)) {
                categoryExists = true;
                break;
            }
        }
        // If the category does not exist, create a new ExpenseCategory object and add it to the categories list
        if (!categoryExists) {
            ExpenseCategory newCategory = new ExpenseCategory(category);
            categories.add(newCategory);
        }
    }
    public List<Expense> getExpenses() {
        return expenses;
    }
    public List<ExpenseCategory> getCategories() {
        return categories;
    }
    /**
     * This method returns a list of all expenses with the given category.
     * @param category The category to filter the expenses by.
     * @return A list of expenses with the given category.
     */
    public List<Expense> getExpensesByCategory(String category) {
        List<Expense> filteredExpenses = new ArrayList<>();
        for (Expense expense : expenses) {
            if (expense.getCategory().equals(category)) {
                filteredExpenses.add(expense);
            }
        }
        return filteredExpenses;
    }
    /**
     * This method calculates and returns the total amount of all expenses.
     * @return The total amount of all expenses.
     */
    public double getTotalExpenses() {
        double totalExpenses = 0.0;
        for (Expense expense : expenses) {
            totalExpenses += expense.getAmount();
        }
        return totalExpenses;
    }
    /**
     * This method calculates and returns the total amount of expenses with the given category.
     * @param category The category to filter the expenses by.
     * @return The total amount of expenses with the given category.
     */
    public double getTotalExpensesByCategory(String category) {
        double totalExpenses = 0.0;
        for (Expense expense : expenses) {
            if (expense.getCategory().equals(category)) {
                totalExpenses += expense.getAmount();
            }
        }
        return totalExpenses;
    }
    /**
     * This method returns a list of all expenses with the given date.
     * @param date The date to filter the expenses by.
     * @return A list of expenses with the given date.
     */
    public List<Expense> getExpensesByDate(String date) {
        List<Expense> filteredExpenses = new ArrayList<>();
        for (Expense expense : expenses) {
            if (expense.getDate().equals(date)) {
                filteredExpenses.add(expense);
            }
        }
        return filteredExpenses;
    }
    /**
     * This method adds an expense with the given amount, category, and date to the expenses list.
     * @param amount The amount of the expense.
     * @param category The category of the expense.
     * @param date The date of the expense.
     */
    public void addExpense(double amount, String category, String date) {
        Expense newExpense = new Expense(amount, category, date);
        expenses.add(newExpense);
    }
}