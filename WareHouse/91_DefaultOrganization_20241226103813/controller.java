import service.Service;
import utility.Utility;
import java.util.Scanner;
/**
 * Controller class for handling user interactions
 */
public class Controller {
    private GUI gui;
    public Controller(GUI gui) {
        this.gui = gui;
    }
    /**
     * Method to handle user interactions
     */
    public void handleUserInteractions() {
        // Capture user input
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter user input: ");
        String userInput = scanner.nextLine();
        scanner.close();
        // Call the appropriate methods from the Service class
        Service service = new Service();
        service.performDataAnalysis();
        service.visualizeData();
        // Update the GUI accordingly
        gui.updateDataVisualization();
    }
}