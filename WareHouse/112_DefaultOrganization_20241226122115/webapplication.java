import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the web application for the Vendor Management System.
 * It handles the user interface and interacts with the database.
 */
public class WebApplication {
    private GUI gui;
    private VendorDatabase vendorDatabase;
    public WebApplication(GUI gui, VendorDatabase vendorDatabase) {
        this.gui = gui;
        this.vendorDatabase = vendorDatabase;
    }
    public void start() {
        gui.setCreateVendorButtonListener(new CreateVendorButtonListener());
        gui.setUpdateVendorButtonListener(new UpdateVendorButtonListener());
        gui.setDeleteVendorButtonListener(new DeleteVendorButtonListener());
        gui.setGenerateReportButtonListener(new GenerateReportButtonListener());
        gui.show();
    }
    private class CreateVendorButtonListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            // Get vendor details from GUI inputs
            String vendorName = gui.getVendorName();
            String vendorEmail = gui.getVendorEmail();
            // Create a new vendor object
            Vendor vendor = new Vendor(vendorName, vendorEmail);
            // Add the vendor to the database
            vendorDatabase.addVendor(vendor);
            // Show success message
            gui.showMessage("Vendor created successfully");
        }
    }
    private class UpdateVendorButtonListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            // Get vendor details from GUI inputs
            String vendorName = gui.getVendorName();
            String vendorEmail = gui.getVendorEmail();
            // Create a new vendor object
            Vendor vendor = new Vendor(vendorName, vendorEmail);
            // Update the vendor in the database
            vendorDatabase.updateVendor(vendor);
            // Show success message
            gui.showMessage("Vendor updated successfully");
        }
    }
    private class DeleteVendorButtonListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            // Get vendor details from GUI inputs
            String vendorName = gui.getVendorName();
            String vendorEmail = gui.getVendorEmail();
            // Create a new vendor object
            Vendor vendor = new Vendor(vendorName, vendorEmail);
            // Delete the vendor from the database
            vendorDatabase.deleteVendor(vendor);
            // Show success message
            gui.showMessage("Vendor deleted successfully");
        }
    }
    private class GenerateReportButtonListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            // Generate report based on vendor performance metrics
            String report = vendorDatabase.generateReport();
            // Show the report in the GUI
            gui.showReport(report);
        }
    }
}