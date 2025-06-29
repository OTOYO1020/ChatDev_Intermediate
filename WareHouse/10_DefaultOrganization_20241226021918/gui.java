/**
 * This class represents the graphical user interface (GUI) of the application.
 */
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JFrame;
import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class GUI extends JPanel {
    private JButton button;
    private JLabel label;
    public GUI() {
        // Set up the main panel
        setLayout(new BorderLayout());
        // Create the button
        button = new JButton("Click Me");
        button.addActionListener(new ButtonClickListener());
        // Create the label
        label = new JLabel("Hello, World!");
        // Add the components to the panel
        add(button, BorderLayout.SOUTH);
        add(label, BorderLayout.CENTER);
    }
    /**
     * This method starts the GUI by making it visible.
     */
    public void start() {
        JFrame frame = new JFrame("Street Fighter");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().add(this);
        frame.pack();
        frame.setVisible(true);
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