package budget;
/**
 * This class represents a budget and contains properties such as category and limit.
 */
public class Budget {
    private String category;
    private double limit;
    public Budget(String category, double limit) {
        this.category = category;
        this.limit = limit;
    }
    public String getCategory() {
        return category;
    }
    public double getLimit() {
        return limit;
    }
}