/**
 * This class represents a vendor in the Vendor Management System.
 */
public class Vendor {
    private String name;
    private String email;
    public Vendor(String name, String email) {
        this.name = name;
        this.email = email;
    }
    public String getName() {
        return name;
    }
    public String getEmail() {
        return email;
    }
}