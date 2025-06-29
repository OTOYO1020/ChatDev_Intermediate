/**
 * This is the main class that contains the entry point of the application.
 * It initializes the GUI and starts the application.
 */
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class Main {
    public static void main(String[] args) {
        // Create an instance of the GUI class
        GUI gui = new GUI();
        // Start the application
        gui.start();
    }
}