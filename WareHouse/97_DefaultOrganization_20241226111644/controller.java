import java.sql.SQLException;
import com.example.Model;
import com.example.GUI;
import com.example.Database;
/**
 * This class handles the user interactions and controls the flow of the web application.
 */
public class Controller {
    private Model model;
    private GUI gui;
    private Database database;
    public Controller() {
        model = new Model();
        gui = new GUI(model);
        database = new Database();
    }
    public void handleUserInput() {
        try {
            // Connect to the database
            database.connect();
            // Code to handle user input and perform necessary actions
            gui.setVisible(true);
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            try {
                database.disconnect();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}