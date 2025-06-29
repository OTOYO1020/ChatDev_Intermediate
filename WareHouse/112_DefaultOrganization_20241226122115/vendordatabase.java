import java.util.ArrayList;
import java.util.List;
/**
 * This class represents the database for storing vendor information.
 */
public class VendorDatabase {
    private List<Vendor> vendors;
    public VendorDatabase() {
        vendors = new ArrayList<>();
    }
    public void addVendor(Vendor vendor) {
        vendors.add(vendor);
    }
    public void updateVendor(Vendor vendor) {
        for (int i = 0; i < vendors.size(); i++) {
            Vendor existingVendor = vendors.get(i);
            if (existingVendor.getName().equals(vendor.getName()) &&
                    existingVendor.getEmail().equals(vendor.getEmail())) {
                vendors.set(i, vendor);
                break;
            }
        }
    }
    public void deleteVendor(Vendor vendor) {
        vendors.removeIf(existingVendor ->
                existingVendor.getName().equals(vendor.getName()) &&
                        existingVendor.getEmail().equals(vendor.getEmail()));
    }
    public String generateReport() {
        StringBuilder report = new StringBuilder();
        for (Vendor vendor : vendors) {
            report.append("Vendor Name: ").append(vendor.getName()).append("\n");
            report.append("Vendor Email: ").append(vendor.getEmail()).append("\n");
            report.append("\n");
        }
        return report.toString();
    }
}