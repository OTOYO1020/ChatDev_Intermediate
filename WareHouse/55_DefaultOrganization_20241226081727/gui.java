'''
This class represents the graphical user interface of the application.
'''
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import controller.Controller;
public class GUI extends JFrame {
    private JTextField inputField;
    private JButton submitButton;
    private JTextArea turnOrderTextArea; // New JTextArea component
    public GUI() {
        setTitle("Board Game Turn Order Randomizer");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());
        inputField = new JTextField(20);
        submitButton = new JButton("Submit");
        turnOrderTextArea = new JTextArea(10, 20); // Initialize JTextArea
        submitButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String input = inputField.getText();
                // Call controller method to handle the input
                Controller.handleInput(input);
            }
        });
        add(inputField);
        add(submitButton);
        add(turnOrderTextArea); // Add JTextArea to the JFrame
        pack();
    }
    public void show() {
        setVisible(true);
    }
    public void showMessage(String message) {
        JOptionPane.showMessageDialog(this, message);
    }
    public void displayTurnOrder(String turnOrder) {
        turnOrderTextArea.setText(turnOrder); // Set the text of the JTextArea
    }
}