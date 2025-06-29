import java.util.*;
/**
 * This class represents the savings target-related operations in the SavingsTracker application.
 */
public class SavingsTarget {
    private double targetAmount;
    public SavingsTarget(double targetAmount) {
        this.targetAmount = targetAmount;
    }
    /**
     * Check if the savings target has been achieved.
     * @param savings The current savings amount.
     * @return True if the savings target has been achieved, false otherwise.
     */
    public boolean isTargetAchieved(double savings) {
        return savings >= targetAmount;
    }
    /**
     * Update the target amount.
     * @param targetAmount The new target amount.
     */
    public void updateTargetAmount(double targetAmount) {
        this.targetAmount = targetAmount;
    }
}