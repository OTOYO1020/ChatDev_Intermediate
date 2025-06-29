import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import CustomerAcquisitionTracker;
/**
 * This class represents the graphical user interface (GUI) for the web application.
 * It creates a window with buttons and handles user interactions.
 */
public class GUI extends JFrame {
    private JButton button;
    private CustomerAcquisitionTracker tracker;
    public GUI(CustomerAcquisitionTracker tracker) {
        // Set up the window
        setTitle("Customer Acquisition Tracker");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Create a button
        button = new JButton("Record Acquisition");
        // Add action listener to the button
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Handle button click event
                recordAcquisition();
            }
        });
        // Add the button to the window
        getContentPane().add(button, BorderLayout.CENTER);
        // Assign the tracker parameter to the instance variable
        this.tracker = tracker;
    }
    public void start() {
        // Show the window
        setVisible(true);
    }
    private void recordAcquisition() {
        // Prompt the user for the acquisition channel
        String channel = JOptionPane.showInputDialog(this, "Enter the acquisition channel:");
        // Record the acquisition
        tracker.recordAcquisition(channel);
        // Display a success message
        JOptionPane.showMessageDialog(this, "Acquisition recorded successfully!");
    }
}