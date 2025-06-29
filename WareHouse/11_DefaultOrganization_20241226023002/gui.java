/**
 * This class represents the graphical user interface of the application.
 */
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import Game.Game; // Add import statement for Game class
public class GUI extends JFrame {
    private JButton button;
    private JLabel label;
    private Game game; // Reference to the Game instance
    public GUI(Game game) {
        this.game = game;
        // Set up the main frame
        setTitle("Application");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(300, 200);
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
    public void start() {
        // Make the frame visible
        setVisible(true);
    }
    private class ButtonClickListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            // Update the label text when the button is clicked
            label.setText("Button Clicked");
            // Request exit from the game
            game.requestExit();
        }
    }
}