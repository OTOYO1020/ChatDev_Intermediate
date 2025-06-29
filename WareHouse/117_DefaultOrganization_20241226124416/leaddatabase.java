import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
/**
 * The LeadDatabase class manages the storage and retrieval of leads.
 */
public class LeadDatabase {
    private Map<LeadCategory, List<Lead>> leadsByCategory;
    public LeadDatabase() {
        leadsByCategory = new HashMap<>();
        for (LeadCategory category : LeadCategory.values()) {
            leadsByCategory.put(category, new ArrayList<>());
        }
    }
    /**
     * Adds a lead to the database.
     *
     * @param lead The lead to be added.
     */
    public void addLead(Lead lead) {
        leadsByCategory.get(lead.getCategory()).add(lead);
    }
    /**
     * Generates a report based on the lead data.
     *
     * @return The generated report.
     */
    public String generateReport() {
        StringBuilder report = new StringBuilder();
        for (LeadCategory category : LeadCategory.values()) {
            List<Lead> leads = leadsByCategory.get(category);
            report.append(category).append(": ").append(leads.size()).append("\n");
        }
        return report.toString();
    }
}