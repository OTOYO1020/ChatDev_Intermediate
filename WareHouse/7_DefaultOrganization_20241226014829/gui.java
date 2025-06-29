import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the graphical user interface of the application.
 * It creates and manages the main window of the application.
 */
public class GUI {
    private JFrame frame;
    private JButton button;
    private GameLogic gameLogic;
    public GUI(GameLogic gameLogic) {
        this.gameLogic = gameLogic;
        // Create the main window
        frame = new JFrame("Application");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        // Create a button
        button = new JButton("Click Me");
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Handle button click event
                showMessage();
            }
        });
        // Add the button to the main window
        frame.getContentPane().add(button, BorderLayout.CENTER);
    }
    public void start() {
        // Display the main window
        frame.setVisible(true);
        // Start the game loop
        gameLogic.start();
    }
    private void showMessage() {
        // Show a message dialog
        JOptionPane.showMessageDialog(frame, "Hello, World!");
    }
}