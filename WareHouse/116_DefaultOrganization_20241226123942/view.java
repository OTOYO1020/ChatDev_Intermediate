/**
 * This class represents the view of the web application.
 * It displays the data from the model and handles user interactions.
 */
import com.example.Model;
import com.example.GUI;
import javax.swing.JOptionPane;
public class View {
    private Model model;
    private GUI gui;
    public View(Model model, GUI gui) {
        this.model = model;
        this.gui = gui;
        // Code to initialize the view and display the data from the model
        updateView();
    }
    // Code for updating the view based on changes in the model
    public void updateView() {
        // Code to update the view based on the model data
        double salesData = model.getSalesData();
        double salesTarget = model.getSalesTarget();
        // For example, you can display the sales data and target in labels
        JOptionPane.showMessageDialog(gui, "Sales Data: " + salesData + "\nSales Target: " + salesTarget);
    }
}