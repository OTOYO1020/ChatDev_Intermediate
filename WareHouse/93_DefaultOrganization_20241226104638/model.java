/**
 * This class represents the data model for the web application.
 */
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
public class Model {
    private List<Task> tasks;
    public Model() {
        tasks = new ArrayList<>();
    }
    /**
     * Adds a task to the model.
     *
     * @param task  the task to add
     */
    public void addTask(Task task) {
        tasks.add(task);
    }
    /**
     * Updates the status of a task in the model.
     *
     * @param task    the task to update
     * @param status  the new status of the task
     */
    public void updateTaskStatus(Task task, String status) {
        task.setStatus(status);
    }
    /**
     * Sets the priority of a task in the model.
     *
     * @param task     the task to prioritize
     * @param priority the priority value of the task
     */
    public void prioritizeTask(Task task, int priority) {
        task.setPriority(priority);
    }
    /**
     * Retrieves the list of tasks assigned to a specific user.
     *
     * @param currentUser  the current user
     * @return             the list of assigned tasks
     */
    public List<Task> getAssignedTasks(String currentUser) {
        List<Task> assignedTasks = new ArrayList<>();
        for (Task task : tasks) {
            if (task.getAssignee().equals(currentUser)) {
                assignedTasks.add(task);
            }
        }
        return assignedTasks;
    }
}