import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the graphical user interface of the web application.
 * It creates a window with buttons and handles user interactions.
 */
public class GUI extends JFrame {
    private JButton button;
    private JTextArea complaintTextArea;
    private JTextArea progressTextArea;
    private JTextArea communicationTextArea;
    private ComplaintManager complaintManager;
    public GUI() {
        // Set up the window
        setTitle("Customer Complaint Resolution Tracker");
        setSize(800, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Create a button
        button = new JButton("Submit Complaint");
        button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Handle button click event
                submitComplaint();
            }
        });
        // Create text areas
        complaintTextArea = new JTextArea(10, 30);
        progressTextArea = new JTextArea(10, 30);
        communicationTextArea = new JTextArea(10, 30);
        // Add the components to the window
        getContentPane().setLayout(new FlowLayout());
        getContentPane().add(new JLabel("Complaint:"));
        getContentPane().add(complaintTextArea);
        getContentPane().add(button);
        getContentPane().add(new JLabel("Progress:"));
        getContentPane().add(progressTextArea);
        getContentPane().add(new JLabel("Communication:"));
        getContentPane().add(communicationTextArea);
        // Initialize the complaint manager
        complaintManager = new ComplaintManager();
    }
    public void start() {
        // Show the window
        setVisible(true);
    }
    private void submitComplaint() {
        String complaintText = complaintTextArea.getText();
        // Create a new complaint
        Complaint complaint = new Complaint(complaintText);
        // Pass the complaint to the complaint manager
        complaintManager.receiveComplaint(complaint);
        // Clear the progress text area
        progressTextArea.setText("");
        // Update the progress text area with the newly submitted complaint
        progressTextArea.append(complaint.getComplaintProgress() + "\n");
    }
}