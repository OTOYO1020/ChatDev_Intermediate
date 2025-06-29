import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import java.awt.FlowLayout;
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
        label = new JLabel("Hello World!");
        // Add the button and label to the frame
        add(button);
        add(label);
    }
    public void start() {
        // Make the frame visible
        setVisible(true);
    }
    private class ButtonClickListener implements ActionListener {
        public void actionPerformed(ActionEvent event) {
            // Change the label text when the button is clicked
            label.setText("Button Clicked!");
        }
    }
}