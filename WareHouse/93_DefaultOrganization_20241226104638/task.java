/**
 * This class represents a task in the web application.
 */
import java.util.Date;
public class Task {
    private String name;
    private String assignee;
    private Date deadline;
    private String status;
    private int priority;
    public Task(String name, String assignee, Date deadline) {
        this.name = name;
        this.assignee = assignee;
        this.deadline = deadline;
        this.status = "Pending";
        this.priority = 0;
    }
    /**
     * Sets the status of the task.
     *
     * @param status  the status of the task
     */
    public void setStatus(String status) {
        this.status = status;
    }
    /**
     * Sets the priority of the task.
     *
     * @param priority  the priority of the task
     */
    public void setPriority(int priority) {
        this.priority = priority;
    }
    /**
     * Retrieves the assignee of the task.
     *
     * @return  the assignee of the task
     */
    public String getAssignee() {
        return assignee;
    }
}