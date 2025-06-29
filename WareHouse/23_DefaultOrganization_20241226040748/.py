import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the graphical user interface (GUI) of the application.
 */
public class GUI {
    private JFrame frame;
    private JButton button;
    private JLabel label;
    public void initialize() {
        // Create the main frame
        frame = new JFrame("Application");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        // Create the button
        button = new JButton("Click Me");
        button.addActionListener(new ButtonClickListener());
        // Create the label
        label = new JLabel("Hello World!");
        // Add the button and label to the frame
        frame.getContentPane().setLayout(new FlowLayout());
        frame.getContentPane().add(button);
        frame.getContentPane().add(label);
        // Make the frame visible
        frame.setVisible(true);
    }
    /**
     * This class represents the action listener for the button.
     */
    private class ButtonClickListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            // Update the label text when the button is clicked
            label.setText("Button Clicked!");
        }
    }
}