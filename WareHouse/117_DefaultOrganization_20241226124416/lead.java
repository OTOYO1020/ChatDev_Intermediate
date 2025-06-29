/**
 * The Lead class represents a lead with properties such as name, contact information, and category.
 */
public class Lead {
    private String name;
    private String contact;
    private LeadCategory category;
    public Lead(String name, String contact, LeadCategory category) {
        this.name = name;
        this.contact = contact;
        this.category = category;
    }
    // Getters and setters for the lead properties
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public String getContact() {
        return contact;
    }
    public void setContact(String contact) {
        this.contact = contact;
    }
    public LeadCategory getCategory() {
        return category;
    }
    public void setCategory(LeadCategory category) {
        this.category = category;
    }
}