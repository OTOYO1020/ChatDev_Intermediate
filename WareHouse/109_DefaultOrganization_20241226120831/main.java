/**
 * This is the main class that contains the entry point of the web application.
 * It initializes the GUI and starts the application.
 */
import javax.swing.*;
import GUI;
public class Main {
    public static void main(String[] args) {
        // Initialize the GUI
        GUI gui = new GUI();
        // Start the application
        gui.start();
    }
}