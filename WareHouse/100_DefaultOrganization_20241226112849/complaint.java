import com.example.complaints.Agent;
import com.example.complaints.Severity;
import com.example.complaints.Status;
/**
 * This class represents a customer complaint.
 */
public class Complaint {
    private String id;
    private String description;
    private Severity severity;
    private Agent assignedAgent;
    private Status status;
    // Constructor
    public Complaint(String id, String description, Severity severity) {
        this.id = id;
        this.description = description;
        this.severity = severity;
        this.status = Status.OPEN;
    }
    // Getters and Setters
    public String getId() {
        return id;
    }
    public String getDescription() {
        return description;
    }
    public Severity getSeverity() {
        return severity;
    }
    public Agent getAssignedAgent() {
        return assignedAgent;
    }
    public void setAssignedAgent(Agent assignedAgent) {
        this.assignedAgent = assignedAgent;
    }
    public Status getStatus() {
        return status;
    }
    public void setStatus(Status status) {
        this.status = status;
    }
    /**
     * Assigns the complaint to the specified agent.
     *
     * @param agent The agent to assign the complaint to.
     */
    public void assignToAgent(Agent agent) {
        this.assignedAgent = agent;
        this.status = Status.IN_PROGRESS;
    }
    /**
     * Escalates the complaint to a higher priority.
     */
    public void escalate() {
        if (severity == Severity.LOW) {
            severity = Severity.MEDIUM;
        } else if (severity == Severity.MEDIUM) {
            severity = Severity.HIGH;
        }
    }
}