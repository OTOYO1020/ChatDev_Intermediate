import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.control.Button;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
public class Main extends Application {
    private PerformanceTracker tracker;
    public static void main(String[] args) {
        launch(args);
    }
    @Override
    public void start(Stage primaryStage) {
        tracker = new PerformanceTracker();
        Employee employee1 = new Employee("John Doe");
        Employee employee2 = new Employee("Jane Smith");
        tracker.addEmployee(employee1);
        tracker.addEmployee(employee2);
        tracker.setPerformanceGoal(employee1, 80);
        tracker.setPerformanceGoal(employee2, 90);
        tracker.conductEvaluation(employee1, 75);
        tracker.conductEvaluation(employee2, 95);
        tracker.generatePerformanceReport();
        // Create GUI elements
        Label nameLabel = new Label("Name:");
        TextField nameTextField = new TextField();
        Button addButton = new Button("Add Employee");
        // Create event handlers
        addButton.setOnAction(e -> {
            String name = nameTextField.getText();
            Employee newEmployee = new Employee(name);
            tracker.addEmployee(newEmployee);
            nameTextField.clear();
        });
        // Create layout and add elements
        VBox root = new VBox(10);
        root.getChildren().addAll(nameLabel, nameTextField, addButton);
        // Create scene and set it on the stage
        Scene scene = new Scene(root, 300, 200);
        primaryStage.setScene(scene);
        primaryStage.setTitle("Employee Performance Tracker");
        primaryStage.show();
    }
}