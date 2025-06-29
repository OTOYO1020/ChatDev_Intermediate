'''
This class is the controller for the GUI components.
'''
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
public class Controller {
    @FXML
    private Button myButton;
    @FXML
    private Label myLabel;
    @FXML
    public void initialize() {
        // Initialize the GUI components
        myButton.setText("Click me!");
        myLabel.setText("");
        // Add event handlers
        myButton.setOnAction(event -> {
            // Handle button click
            myLabel.setText("Button clicked!");
        });
    }
}