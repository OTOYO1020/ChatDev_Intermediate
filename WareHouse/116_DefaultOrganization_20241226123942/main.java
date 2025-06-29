/**
 * This is the main class that initializes the web application.
 */
import com.example.Model;
import com.example.GUI;
import com.example.Controller;
import com.example.View;
public class Main {
    public static void main(String[] args) {
        Model model = new Model();
        GUI gui = new GUI();
        View view = new View(model, gui);
        Controller controller = new Controller(model, gui, view);
        // Code to initialize the web application
        // For example, you can set up the GUI and start the event loop
        gui.setVisible(true);
    }
}