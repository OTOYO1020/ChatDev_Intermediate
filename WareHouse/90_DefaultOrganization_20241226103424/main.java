/**
 * This is the main class that serves as the entry point of the web application.
 * It initializes the GUI and starts the application.
 */
import javax.swing.*;
import BudgetAssistant.BudgetAssistant;
import GUI.GUI;
public class Main {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                BudgetAssistant budgetAssistant = new BudgetAssistant();
                GUI gui = new GUI(budgetAssistant);
                budgetAssistant.start(gui);
            }
        });
    }
}