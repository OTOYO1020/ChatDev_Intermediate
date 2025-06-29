import javax.swing.SwingUtilities;
import GUI.GUI;
public class BudgetAssistant {
    public void start(GUI gui) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                gui.setVisible(true);
            }
        });
    }
    public double analyzeBudget(double income, double expenses) {
        double savings = income - expenses;
        // Add logic for analyzing the budget and providing recommendations
        if (expenses > income) {
            System.out.println("You are spending more than your income. Consider reducing expenses.");
        } else {
            System.out.println("You are saving money. Keep up the good work!");
        }
        return savings;
    }
}