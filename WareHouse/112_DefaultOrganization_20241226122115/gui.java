import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionListener;
/**
 * This class represents the graphical user interface for the Vendor Management System.
 */
public class GUI {
    private JFrame frame;
    private JTextField vendorNameField;
    private JTextField vendorEmailField;
    private JButton createVendorButton;
    private JButton updateVendorButton;
    private JButton deleteVendorButton;
    private JButton generateReportButton;
    private JTextArea reportArea;
    public GUI() {
        frame = new JFrame("Vendor Management System");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new FlowLayout());
        JLabel vendorNameLabel = new JLabel("Vendor Name:");
        vendorNameField = new JTextField(20);
        JLabel vendorEmailLabel = new JLabel("Vendor Email:");
        vendorEmailField = new JTextField(20);
        createVendorButton = new JButton("Create Vendor");
        updateVendorButton = new JButton("Update Vendor");
        deleteVendorButton = new JButton("Delete Vendor");
        generateReportButton = new JButton("Generate Report");
        reportArea = new JTextArea(10, 30);
        reportArea.setEditable(false);
        frame.add(vendorNameLabel);
        frame.add(vendorNameField);
        frame.add(vendorEmailLabel);
        frame.add(vendorEmailField);
        frame.add(createVendorButton);
        frame.add(updateVendorButton);
        frame.add(deleteVendorButton);
        frame.add(generateReportButton);
        frame.add(reportArea);
        frame.pack();
        frame.setVisible(false);
    }
    public void setCreateVendorButtonListener(ActionListener listener) {
        createVendorButton.addActionListener(listener);
    }
    public void setUpdateVendorButtonListener(ActionListener listener) {
        updateVendorButton.addActionListener(listener);
    }
    public void setDeleteVendorButtonListener(ActionListener listener) {
        deleteVendorButton.addActionListener(listener);
    }
    public void setGenerateReportButtonListener(ActionListener listener) {
        generateReportButton.addActionListener(listener);
    }
    public String getVendorName() {
        return vendorNameField.getText();
    }
    public String getVendorEmail() {
        return vendorEmailField.getText();
    }
    public void showMessage(String message) {
        JOptionPane.showMessageDialog(frame, message);
    }
    public void showReport(String report) {
        reportArea.setText(report);
    }
    public void show() {
        frame.setVisible(true);
    }
}