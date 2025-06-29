/**
 * This class represents a user of the BudgetOptimizerPlus application.
 */
public class User {
    private double savingsGoal;
    private double savingsProgress;
    /**
     * Constructor for User class.
     */
    public User() {
        // Initialize savings goal and progress to 0
        savingsGoal = 0;
        savingsProgress = 0;
    }
    /**
     * Set the user's savings goal.
     *
     * @param savingsGoal The savings goal to be set
     */
    public void setSavingsGoal(double savingsGoal) {
        this.savingsGoal = savingsGoal;
    }
    /**
     * Get the user's savings goal.
     *
     * @return The user's savings goal
     */
    public double getSavingsGoal() {
        return savingsGoal;
    }
    /**
     * Get the user's savings progress.
     *
     * @return The user's savings progress
     */
    public double getSavingsProgress() {
        return savingsProgress;
    }
}