/**
 * This class represents a savings goal with its target amount and target date.
 */
public class SavingsGoal {
    private double targetAmount;
    private String targetDate;
    public SavingsGoal(double targetAmount, String targetDate) {
        this.targetAmount = targetAmount;
        this.targetDate = targetDate;
    }
    public double getTargetAmount() {
        return targetAmount;
    }
    public String getTargetDate() {
        return targetDate;
    }
}