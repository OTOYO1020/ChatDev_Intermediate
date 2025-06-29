import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the graphical user interface of the SmartBudget application.
 */
public class GUI extends JFrame {
    private JLabel recommendationLabel;
    private JButton calculateButton;
    private BudgetManager budgetManager;
    public GUI() {
        // Set up the GUI window
        setTitle("SmartBudget");
        setSize(400, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());
        // Create the recommendation label
        recommendationLabel = new JLabel("Click the button to calculate your spending recommendation.");
        add(recommendationLabel);
        // Create the calculate button
        calculateButton = new JButton("Calculate");
        calculateButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Perform budgeting calculation
                if (budgetManager != null) {
                    String recommendation = budgetManager.calculateRecommendation();
                    recommendationLabel.setText("Your spending recommendation is: " + recommendation);
                } else {
                    recommendationLabel.setText("BudgetManager is not properly initialized.");
                }
            }
        });
        add(calculateButton);
        // Create an instance of the BudgetManager class
        budgetManager = new BudgetManager();
    }
    public void start() {
        // Make the GUI window visible
        setVisible(true);
    }
}