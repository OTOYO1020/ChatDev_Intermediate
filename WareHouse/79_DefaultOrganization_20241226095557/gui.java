package com.example.budgetsaverlite;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the graphical user interface (GUI) for the application.
 * It contains the main window and handles user interactions.
 */
public class GUI extends JPanel implements ActionListener {
    private JButton button;
    public GUI() {
        // Create a button
        button = new JButton("Click Me");
        button.addActionListener(this);
        // Add the button to the panel
        add(button);
    }
    @Override
    public void actionPerformed(ActionEvent e) {
        // Handle button click event
        showMessage();
    }
    private void showMessage() {
        // Display a message dialog
        JOptionPane.showMessageDialog(this, "Hello, World!", "Message", JOptionPane.INFORMATION_MESSAGE);
    }
}