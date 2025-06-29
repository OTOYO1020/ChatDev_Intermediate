/**
 * This class acts as a controller for the web application.
 * It handles user interactions and updates the model and view accordingly.
 */
import com.example.Model;
import com.example.GUI;
import com.example.View;
public class Controller {
    private Model model;
    private GUI gui;
    private View view;
    public Controller(Model model, GUI gui, View view) {
        this.model = model;
        this.gui = gui;
        this.view = view;
        // Code to initialize the controller and set up event listeners
        gui.getInputButton().addActionListener(e -> handleInputButton());
        gui.getGenerateButton().addActionListener(e -> handleGenerateButton());
        gui.getVisualizeButton().addActionListener(e -> handleVisualizeButton());
    }
    // Code for handling user interactions and updating the model and view
    private void handleInputButton() {
        // Code to handle the input button click event
        // For example, you can open a dialog to input sales data
        String input = JOptionPane.showInputDialog(gui, "Enter sales data:");
        if (input != null) {
            try {
                double salesData = Double.parseDouble(input);
                model.setSalesData(salesData);
                view.updateView();
            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(gui, "Invalid input! Please enter a numeric value.");
            }
        } else {
            // Handle the case when the user cancels the input dialog
            // For example, you can display a message or perform some other action
            JOptionPane.showMessageDialog(gui, "Input canceled!");
            // Clear the sales data in the model
            model.setSalesData(0.0);
            // Update the view to reflect the changes
            view.updateView();
        }
    }
    private void handleGenerateButton() {
        // Code to handle the generate button click event
        // For example, you can generate reports based on the sales data
        double salesData = model.getSalesData();
        double salesTarget = model.getSalesTarget();
        // Generate reports based on the sales data and target
        // Display the reports to the user
        JOptionPane.showMessageDialog(gui, "Reports generated:\nSales Data: " + salesData + "\nSales Target: " + salesTarget);
    }
    private void handleVisualizeButton() {
        // Code to handle the visualize button click event
        // For example, you can display charts or graphs to visualize sales performance
        double salesData = model.getSalesData();
        double salesTarget = model.getSalesTarget();
        // Visualize the sales performance using charts or graphs
        // Display the visualization to the user
        JOptionPane.showMessageDialog(gui, "Sales Performance Visualization:\nSales Data: " + salesData + "\nSales Target: " + salesTarget);
    }
}