import java.util.*;
/**
 * This class represents the income-related operations in the SavingsTracker application.
 */
public class Income {
    private List<Double> incomes;
    public Income() {
        incomes = new ArrayList<>();
    }
    /**
     * Add income amount to the list of incomes.
     * @param amount The income amount to be added.
     */
    public void addIncome(double amount) {
        incomes.add(amount);
    }
    /**
     * Calculate the total income.
     * @return The total income.
     */
    public double calculateTotalIncome() {
        return incomes.stream().mapToDouble(Double::doubleValue).sum();
    }
    /**
     * Get the list of incomes.
     * @return The list of incomes.
     */
    public List<Double> getIncomes() {
        return incomes;
    }
}