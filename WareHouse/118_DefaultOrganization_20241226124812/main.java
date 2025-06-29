/**
 * This is the main class that serves as the entry point of the application.
 * It initializes the GUI and starts the application.
 */
public class Main {
    public static void main(String[] args) {
        // Create an instance of the GUI class
        GUI gui = new GUI();
        // Start the application
        SwingUtilities.invokeLater(gui::start);
    }
}