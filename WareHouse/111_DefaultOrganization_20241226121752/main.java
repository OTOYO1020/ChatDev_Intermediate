/**
 * This is the main class that serves as the entry point for the web application.
 * It initializes the GUI and starts the application.
 */
import javax.swing.*;
import GUI.GUI;
import CustomerAcquisitionTracker;
public class Main {
    public static void main(String[] args) {
        // Create an instance of CustomerAcquisitionTracker
        CustomerAcquisitionTracker tracker = new CustomerAcquisitionTracker();
        // Initialize the GUI with the tracker instance
        GUI gui = new GUI(tracker);
        // Start the application
        gui.start();
    }
}