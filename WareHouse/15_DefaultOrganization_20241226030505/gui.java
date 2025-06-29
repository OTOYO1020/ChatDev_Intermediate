/**
 * This class represents the graphical user interface (GUI) for the application.
 * It contains the main window and handles user interactions.
 */
import javax.swing.JFrame;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JLabel;
public class GUI extends JFrame {
    private JButton button;
    private JLabel label;
    public GUI() {
        // Set up the main window
        setTitle("Dungeon Hero");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(400, 300);
        setLayout(new FlowLayout());
        // Create the button
        button = new JButton("Click Me");
        // Create the label
        label = new JLabel("Hello World");
        // Add the button and label to the main window
        add(button);
        add(label);
        // Add action listener to the button
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Handle button click event
                label.setText("Button Clicked");
            }
        });
    }
    public void start() {
        // Make the main window visible
        setVisible(true);
    }
}