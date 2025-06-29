/**
 * This is the main class that serves as the entry point for the web application.
 * It initializes the GUI and starts the application.
 */
import GUI.GUI;
import feedback.FeedbackFormManager;
import feedback.FeedbackDataAnalyzer;
public class Main {
    public static void main(String[] args) {
        // Create an instance of the GUI class
        GUI gui = new GUI(new FeedbackFormManager(), new FeedbackDataAnalyzer());
        // Start the application
        gui.start();
    }
}