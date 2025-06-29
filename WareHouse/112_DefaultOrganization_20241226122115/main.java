/**
 * This class is the entry point of the Vendor Management System application.
 */
public class Main {
    public static void main(String[] args) {
        GUI gui = new GUI();
        VendorDatabase vendorDatabase = new VendorDatabase();
        WebApplication webApplication = new WebApplication(gui, vendorDatabase);
        webApplication.start();
    }
}