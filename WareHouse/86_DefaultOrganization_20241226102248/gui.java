import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the graphical user interface (GUI) of the BudgetEnforcer application.
 * It contains the main window and handles user interactions.
 */
public class GUI {
    private JFrame frame;
    private JButton button;
    private JLabel label;
    public GUI() {
        // Create the main window
        frame = new JFrame("BudgetEnforcer");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        // Create a button
        button = new JButton("Click me");
        button.addActionListener(new ButtonClickListener());
        // Create a label
        label = new JLabel("Hello, World!");
        // Add the button and label to the main window
        frame.getContentPane().setLayout(new FlowLayout());
        frame.getContentPane().add(button);
        frame.getContentPane().add(label);
    }
    public void start() {
        // Display the main window
        frame.setVisible(true);
    }
    private class ButtonClickListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            // Handle button click event
            label.setText("Button clicked");
        }
    }
}