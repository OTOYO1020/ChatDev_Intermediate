import com.example.complaints.Complaint;
/**
 * This class represents a ticket for a customer complaint.
 */
public class Ticket {
    private Complaint complaint;
    private boolean escalated;
    // Constructor
    public Ticket(Complaint complaint) {
        this.complaint = complaint;
        this.escalated = false;
    }
    // Getters and Setters
    public Complaint getComplaint() {
        return complaint;
    }
    public boolean isEscalated() {
        return escalated;
    }
    public void setEscalated(boolean escalated) {
        this.escalated = escalated;
    }
    /**
     * Escalates the ticket to a higher priority.
     */
    public void escalate() {
        escalated = true;
    }
}