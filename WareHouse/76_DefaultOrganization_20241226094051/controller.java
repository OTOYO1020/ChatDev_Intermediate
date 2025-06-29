'''
This class handles user interactions and controls the flow of the BudgetTrackerLite application.
'''
import javax.swing.*;
public class Controller {
    private GUI gui;
    private DataManager dataManager;
    public Controller(GUI gui, DataManager dataManager) {
        this.gui = gui;
        this.dataManager = dataManager;
    }
    public void deleteBudgetItem(int index) {
        if (index >= 0 && index < dataManager.getBudgetItems().size()) {
            dataManager.deleteBudgetItem(index);
            gui.updateBudgetList();
            gui.updateSummaryLabels();
        } else {
            // Handle the case when the index is out of bounds
            // You can display an error message or throw an exception
            // depending on your application's requirements
            JOptionPane.showMessageDialog(null, "Invalid index!");
        }
    }
    public void updateBudgetGoal(double goal) {
        dataManager.setBudgetGoal(goal);
        gui.updateSummaryLabels();
    }
    public void generateBudgetBreakdown() {
        // Generate visual representations of budget breakdowns
        // ...
        JOptionPane.showMessageDialog(null, "Budget breakdown generated!");
    }
}