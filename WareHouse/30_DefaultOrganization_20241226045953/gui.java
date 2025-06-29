import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the graphical user interface of the application.
 */
public class GUI extends JFrame {
    private JButton button;
    private JLabel label;
    public GUI() {
        // Set up the main frame
        setTitle("Application");
        setSize(300, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());
        // Create the button
        button = new JButton("Click Me");
        button.addActionListener(new ButtonClickListener());
        // Create the label
        label = new JLabel("Hello, World!");
        // Add the components to the frame
        add(button);
        add(label);
    }
    /**
     * This method starts the GUI application.
     */
    public void start() {
        setVisible(true);
    }
    /**
     * This class represents the action listener for the button.
     */
    private class ButtonClickListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            // Update the label text when the button is clicked
            label.setText("Button Clicked");
        }
    }
}