/**
 * This class handles the business logic and acts as a controller for the web application.
 */
import java.util.Date;
import java.util.List;
public class Controller {
    private Model model;
    private View view;
    public Controller(Model model, View view) {
        this.model = model;
        this.view = view;
    }
    /**
     * Creates a new task and adds it to the model.
     *
     * @param taskName  the name of the task
     * @param assignee  the assignee of the task
     * @param deadline  the deadline of the task
     */
    public void createTask(String taskName, String assignee, Date deadline) {
        Task task = new Task(taskName, assignee, deadline);
        model.addTask(task);
    }
    /**
     * Updates the status of a task in the model.
     *
     * @param task    the task to update
     * @param status  the new status of the task
     */
    public void updateTaskStatus(Task task, String status) {
        model.updateTaskStatus(task, status);
    }
    /**
     * Sets the priority of a task in the model.
     *
     * @param task     the task to prioritize
     * @param priority the priority value of the task
     */
    public void prioritizeTask(Task task, int priority) {
        model.prioritizeTask(task, priority);
    }
    /**
     * Displays the dashboard for a specific user.
     *
     * @param currentUser  the current user
     */
    public void displayDashboard(String currentUser) {
        List<Task> tasks = model.getAssignedTasks(currentUser);
        view.showDashboard(tasks);
    }
}