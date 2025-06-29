/**
 * This class represents a customer complaint.
 */
public class Complaint {
    private static int nextId = 1;
    private int id;
    private String description;
    private String severity;
    private String status;
    private String assignedAgent;
    public Complaint(String description) {
        this.id = nextId++;
        this.description = description;
        this.severity = "Low";
        this.status = "Open";
        this.assignedAgent = "Unassigned";
    }
    public int getId() {
        return id;
    }
    public String getDescription() {
        return description;
    }
    public String getSeverity() {
        return severity;
    }
    public void setSeverity(String severity) {
        this.severity = severity;
    }
    public String getStatus() {
        return status;
    }
    public void setStatus(String status) {
        this.status = status;
    }
    public String getAssignedAgent() {
        return assignedAgent;
    }
    public void setAssignedAgent(String assignedAgent) {
        this.assignedAgent = assignedAgent;
    }
    public String getComplaintProgress() {
        StringBuilder progress = new StringBuilder();
        progress.append("Complaint ID: ").append(getId()).append("\n");
        progress.append("Description: ").append(getDescription()).append("\n");
        progress.append("Severity: ").append(getSeverity()).append("\n");
        progress.append("Status: ").append(getStatus()).append("\n");
        progress.append("Assigned Agent: ").append(getAssignedAgent()).append("\n");
        progress.append("\n");
        return progress.toString();
    }
}