import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
public class GUI extends Application {
    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("My Application");
        Button button = new Button("Click Me");
        button.setOnAction(e -> System.out.println("Button clicked!"));
        VBox layout = new VBox(10);
        layout.getChildren().add(button);
        Scene scene = new Scene(layout, 300, 200);
        primaryStage.setScene(scene);
        primaryStage.show();
    }
}