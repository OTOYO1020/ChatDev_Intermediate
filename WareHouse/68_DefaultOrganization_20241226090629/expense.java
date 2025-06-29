/**
 * This class represents an expense with its amount, category, and date.
 */
public class Expense {
    private double amount;
    private String category;
    private String date;
    public Expense(double amount, String category, String date) {
        this.amount = amount;
        this.category = category;
        this.date = date;
    }
    public double getAmount() {
        return amount;
    }
    public String getCategory() {
        return category;
    }
    public String getDate() {
        return date;
    }
}