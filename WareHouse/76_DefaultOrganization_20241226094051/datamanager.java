'''
This class manages the data storage and retrieval for the BudgetTrackerLite application.
'''
import java.util.ArrayList;
import java.util.List;
public class DataManager {
    private List<BudgetItem> budgetItems;
    private double budgetGoal;
    public DataManager() {
        budgetItems = new ArrayList<>();
        budgetGoal = 0;
    }
    public void addBudgetItem(double income, double expense) {
        BudgetItem item = new BudgetItem(income, expense);
        budgetItems.add(item);
    }
    public void deleteBudgetItem(int index) {
        if (index >= 0 && index < budgetItems.size()) {
            budgetItems.remove(index);
        } else {
            // Handle the case when the index is out of bounds
            // You can display an error message or throw an exception
            // depending on your application's requirements
            JOptionPane.showMessageDialog(null, "Invalid index!");
        }
    }
    public void setBudgetGoal(double goal) {
        budgetGoal = goal;
    }
    public List<BudgetItem> getBudgetItems() {
        return budgetItems;
    }
    public double getTotalIncome() {
        double totalIncome = 0;
        for (BudgetItem item : budgetItems) {
            totalIncome += item.getIncome();
        }
        return totalIncome;
    }
    public double getTotalExpense() {
        double totalExpense = 0;
        for (BudgetItem item : budgetItems) {
            totalExpense += item.getExpense();
        }
        return totalExpense;
    }
    public double getBudgetGoal() {
        return budgetGoal;
    }
}