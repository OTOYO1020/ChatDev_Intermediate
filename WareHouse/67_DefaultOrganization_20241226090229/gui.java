import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the graphical user interface (GUI) for the application.
 * It contains the main window and handles user interactions.
 */
public class GUI {
    private JFrame frame;
    private JButton button;
    private JLabel label;
    public GUI() {
        // Create the main window
        frame = new JFrame("BudgetMonitor");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        frame.setLayout(new FlowLayout());
        // Create a button
        button = new JButton("Click Me");
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Handle button click event
                label.setText("Button clicked!");
            }
        });
        // Create a label
        label = new JLabel("Hello World!");
        // Add the button and label to the frame
        frame.add(button);
        frame.add(label);
    }
    public void start() {
        // Make the frame visible
        frame.setVisible(true);
    }
    public JFrame getFrame() {
        return frame;
    }
}