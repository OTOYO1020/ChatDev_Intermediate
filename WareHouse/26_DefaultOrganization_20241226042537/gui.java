import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * GUI class to create the game's graphical user interface
 */
public class GUI {
    private JFrame frame;
    private JButton button;
    public GUI() {
        // Initialize the frame and button
        frame = new JFrame("Galactic Defender");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(800, 600);
        button = new JButton("Click me");
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                showMessage("Button clicked!");
            }
        });
        frame.getContentPane().add(button, BorderLayout.CENTER);
    }
    public void start() {
        // Make the frame visible
        frame.setVisible(true);
    }
    private void showMessage(String message) {
        // Show a message dialog with the given message
        JOptionPane.showMessageDialog(frame, message);
    }
}