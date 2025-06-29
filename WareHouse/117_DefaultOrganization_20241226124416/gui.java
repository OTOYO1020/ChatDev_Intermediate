import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ComboBox;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import com.example.LeadDatabase;
import com.example.Lead;
import com.example.LeadCategory;
public class GUI extends Application {
    private LeadDatabase leadDatabase;
    @Override
    public void start(Stage primaryStage) {
        // Create the main layout
        VBox layout = new VBox();
        // Create text fields for lead information
        TextField nameTextField = new TextField();
        TextField contactTextField = new TextField();
        // Create a combo box for lead category selection
        ComboBox<LeadCategory> categoryComboBox = new ComboBox<>();
        categoryComboBox.getItems().addAll(LeadCategory.values());
        // Create a button for adding leads
        Button addButton = new Button("Add Lead");
        addButton.setOnAction(e -> {
            // Create a new lead object with the entered information
            Lead lead = new Lead(nameTextField.getText(), contactTextField.getText(), categoryComboBox.getValue());
            // Add the lead to the database
            leadDatabase.addLead(lead);
            // Clear the text fields
            nameTextField.clear();
            contactTextField.clear();
        });
        // Create a label for displaying the number of leads in each category
        Label categoryCountLabel = new Label();
        // Create a button for generating lead reports
        Button generateReportButton = new Button("Generate Report");
        generateReportButton.setOnAction(e -> {
            // Generate the report based on the lead data
            String report = leadDatabase.generateReport();
            // Display the report in a new window or save it to a file
            // (implementation details depend on the requirements)
            System.out.println(report);
        });
        // Add the UI components to the layout
        layout.getChildren().addAll(nameTextField, contactTextField, categoryComboBox, addButton, categoryCountLabel, generateReportButton);
        // Create the scene
        Scene scene = new Scene(layout, 400, 300);
        // Set the scene on the stage
        primaryStage.setScene(scene);
        // Set the title of the stage
        primaryStage.setTitle("Lead Generation Tracker");
        // Initialize the lead database
        leadDatabase = new LeadDatabase();
        // Show the stage
        primaryStage.show();
    }
    public static void main(String[] args) {
        // Launch the application
        launch(args);
    }
}