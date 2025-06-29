import java.util.ArrayList;
import java.util.List;
/**
 * This class manages the customer complaints.
 */
public class ComplaintManager {
    private List<Complaint> complaints;
    public ComplaintManager() {
        complaints = new ArrayList<>();
    }
    public void receiveComplaint(Complaint complaint) {
        complaints.add(complaint);
    }
    public void assignComplaint(Complaint complaint, String agentName) {
        complaint.setAssignedAgent(agentName);
    }
    public List<Complaint> getComplaints() {
        return complaints;
    }
}