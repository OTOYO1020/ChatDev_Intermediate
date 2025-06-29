import java.util.ArrayList;
import java.util.List;
/**
 * This class manages the complaints and their assignments.
 */
public class ComplaintManager {
    private List<Complaint> complaints;
    private List<Agent> agents;
    public ComplaintManager() {
        this.complaints = new ArrayList<>();
        this.agents = new ArrayList<>();
    }
    public void createComplaint(String description, Severity severity) {
        String id = generateComplaintId();
        Complaint complaint = new Complaint(id, description, severity);
        complaints.add(complaint);
    }
    public List<Complaint> getAllComplaints() {
        return complaints;
    }
    private String generateComplaintId() {
        // Generate a unique complaint id
        return "COM-" + (complaints.size() + 1);
    }
}