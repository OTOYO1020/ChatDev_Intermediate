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
    public GUI() {
        // Create the main window
        frame = new JFrame("Dragon Fury");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(800, 600);
        // Create a button
        button = new JButton("Click Me");
        button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Handle button click event
                showMessage();
            }
        });
        // Add the button to the main window
        frame.getContentPane().add(button, BorderLayout.CENTER);
    }
    public void start() {
        // Show the main window
        frame.setVisible(true);
    }
    private void showMessage() {
        // Show a message dialog
        JOptionPane.showMessageDialog(frame, "Hello, Dragon Fury!");
    }
}