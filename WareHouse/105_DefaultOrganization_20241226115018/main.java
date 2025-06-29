'''
This is the main class that launches the JavaFX application.
'''
import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
public class Main extends Application {
    @Override
    public void start(Stage primaryStage) throws Exception {
        // Load the FXML file
        Parent root = FXMLLoader.load(getClass().getResource("view.fxml"));
        // Create the scene
        Scene scene = new Scene(root);
        // Set the scene on the stage
        primaryStage.setScene(scene);
        primaryStage.setTitle("Customer Satisfaction Index Tracker");
        primaryStage.show();
    }
    /**
     * The main entry point for the application.
     * Launches the JavaFX application.
     */
    public static void main(String[] args) {
        launch(args);
    }
}