'''
This class is the main entry point for the Project Tracker application.
'''
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
public class ProjectTracker extends Application {
    @Override
    public void start(Stage primaryStage) throws Exception {
        // Load the FXML file
        FXMLLoader loader = new FXMLLoader(getClass().getResource("myview.fxml"));
        Parent root = loader.load();
        // Set the controller for the FXML file
        Controller controller = loader.getController();
        // Create the scene and set it on the stage
        Scene scene = new Scene(root, 800, 600);
        primaryStage.setScene(scene);
        primaryStage.setTitle("Project Tracker");
        primaryStage.show();
    }
    public static void main(String[] args) {
        launch(args);
    }
}