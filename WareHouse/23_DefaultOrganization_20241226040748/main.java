/**
 * This is the main class that initializes the application and GUI.
 */
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class Main {
    public static void main(String[] args) {
        // Create an instance of the GUI class
        GUI gui = new GUI();
        // Initialize the GUI
        gui.initialize();
    }
}