import java.util.ArrayList;
import java.util.List;
/**
 * This class represents a savings tracker that tracks savings goals and progress.
 */
public class SavingsTracker {
    private List<SavingsGoal> goals;
    public SavingsTracker() {
        goals = new ArrayList<>();
    }
    public void addGoal(double targetAmount, String targetDate) {
        // Create a new SavingsGoal object and add it to the goals list
        SavingsGoal newGoal = new SavingsGoal(targetAmount, targetDate);
        goals.add(newGoal);
    }
    public List<SavingsGoal> getGoals() {
        return goals;
    }
    /**
     * This method returns a list of all goals with the given target date.
     * @param targetDate The target date to filter the goals by.
     * @return A list of goals with the given target date.
     */
    public List<SavingsGoal> getGoalsByDate(String targetDate) {
        List<SavingsGoal> filteredGoals = new ArrayList<>();
        for (SavingsGoal goal : goals) {
            if (goal.getTargetDate().equals(targetDate)) {
                filteredGoals.add(goal);
            }
        }
        return filteredGoals;
    }
    /**
     * This method calculates and returns the total amount of all goals.
     * @return The total amount of all goals.
     */
    public double getTotalGoals() {
        double totalGoals = 0.0;
        for (SavingsGoal goal : goals) {
            totalGoals += goal.getTargetAmount();
        }
        return totalGoals;
    }
    /**
     * This method calculates and returns the progress towards the savings goals as a percentage.
     * @return The progress towards the savings goals as a percentage.
     */
    public double getProgress() {
        double totalGoals = getTotalGoals();
        double totalProgress = 0.0;
        for (SavingsGoal goal : goals) {
            totalProgress += goal.getTargetAmount() / totalGoals;
        }
        return totalProgress * 100;
    }
}