import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the GUI for the Battle Squad game.
 */
public class GUI extends JFrame {
    public GUI() {
        setTitle("Battle Squad");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(800, 600);
        setLocationRelativeTo(null);
        // Create a panel to hold the game components
        JPanel panel = new JPanel();
        panel.setLayout(new BorderLayout());
        // Add your game components to the panel
        JLabel label = new JLabel("Welcome to Battle Squad!");
        panel.add(label, BorderLayout.CENTER);
        // Add the panel to the frame
        add(panel);
        setVisible(true);
    }
}