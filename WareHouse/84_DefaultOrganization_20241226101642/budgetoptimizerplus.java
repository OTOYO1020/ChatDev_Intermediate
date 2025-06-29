/**
 * This class represents the BudgetOptimizerPlus application.
 */
public class BudgetOptimizerPlus {
    private User user;
    private Recommendations recommendations;
    /**
     * Constructor for BudgetOptimizerPlus class.
     */
    public BudgetOptimizerPlus() {
        // Initialize the User and Recommendations classes
        user = new User();
        recommendations = new Recommendations();
    }
    /**
     * Get personalized recommendations based on user's spending patterns and financial habits.
     *
     * @return The personalized recommendations
     */
    public String getRecommendations() {
        // Logic to generate personalized recommendations
        return recommendations.generate(user);
    }
    /**
     * Set the user's savings goal.
     *
     * @param savingsGoal The savings goal to be set
     */
    public void setSavingsGoal(double savingsGoal) {
        user.setSavingsGoal(savingsGoal);
    }
    /**
     * Get the user's savings goal.
     *
     * @return The user's savings goal
     */
    public double getSavingsGoal() {
        return user.getSavingsGoal();
    }
    /**
     * Get the user's savings progress.
     *
     * @return The user's savings progress
     */
    public double getSavingsProgress() {
        return user.getSavingsProgress();
    }
}