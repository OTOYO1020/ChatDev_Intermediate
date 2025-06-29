'''
This class represents the main application window.
'''
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
public class MyApp extends Application {
    @Override
    public void start(Stage primaryStage) {
        // Create the main layout
        VBox root = new VBox();
        // Add components to the layout
        // Create the scene and set it on the stage
        Scene scene = new Scene(root, 800, 600);
        primaryStage.setScene(scene);
        primaryStage.setTitle("Project Tracker");
        primaryStage.show();
    }
}