/**
 * This is the main class that serves as the entry point for the application.
 * It initializes the GUI and starts the application.
 */
import javax.swing.*;
import java.awt.*;
import GUI.GUI;
public class Main {
    public static void main(String[] args) {
        GUI gui = new GUI();
        gui.start();
    }
}