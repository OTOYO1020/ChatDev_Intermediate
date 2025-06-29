import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the graphical user interface (GUI) for the application.
 * It creates a window with buttons and handles user interactions.
 */
public class GUI extends JFrame {
    private JButton button;
    public GUI() {
        // Set up the window
        setTitle("Ninja Duel");
        setSize(800, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Create a button
        button = new JButton("Click me");
        // Add an action listener to the button
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Handle button click event
                showMessage();
            }
        });
        // Add the button to the window
        getContentPane().add(button, BorderLayout.CENTER);
    }
    public void start() {
        // Show the window
        setVisible(true);
    }
    private void showMessage() {
        // Display a message dialog
        JOptionPane.showMessageDialog(this, "Button clicked!");
    }
}