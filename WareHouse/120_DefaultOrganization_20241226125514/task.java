/**
 * This class represents a task in the Business Task Scheduler application.
 * It includes properties for task name, task description, deadline, priority, and progress.
 */
public class Task {
    private String name;
    private String description;
    private String deadline;
    private int priority;
    private int progress;
    /**
     * Constructor for the Task class.
     * Initializes the task with the given name and description.
     * The deadline is initially set to null.
     *
     * @param name        The name of the task
     * @param description The description of the task
     */
    public Task(String name, String description) {
        this.name = name;
        this.description = description;
        this.deadline = null;
        this.priority = 0;
        this.progress = 0;
    }
    /**
     * Method to get the name of the task.
     *
     * @return The name of the task
     */
    public String getName() {
        return name;
    }
    /**
     * Method to set the name of the task.
     *
     * @param name The name of the task
     */
    public void setName(String name) {
        this.name = name;
    }
    /**
     * Method to get the description of the task.
     *
     * @return The description of the task
     */
    public String getDescription() {
        return description;
    }
    /**
     * Method to set the description of the task.
     *
     * @param description The description of the task
     */
    public void setDescription(String description) {
        this.description = description;
    }
    /**
     * Method to get the deadline of the task.
     *
     * @return The deadline of the task
     */
    public String getDeadline() {
        return deadline;
    }
    /**
     * Method to set the deadline of the task.
     *
     * @param deadline The deadline of the task
     */
    public void setDeadline(String deadline) {
        this.deadline = deadline;
    }
    /**
     * Method to get the priority of the task.
     *
     * @return The priority of the task
     */
    public int getPriority() {
        return priority;
    }
    /**
     * Method to set the priority of the task.
     *
     * @param priority The priority of the task
     */
    public void setPriority(int priority) {
        this.priority = priority;
    }
    /**
     * Method to get the progress of the task.
     *
     * @return The progress of the task
     */
    public int getProgress() {
        return progress;
    }
    /**
     * Method to set the progress of the task.
     *
     * @param progress The progress of the task
     */
    public void setProgress(int progress) {
        this.progress = progress;
    }
}