import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import javax.swing.*;
/**
 * This class represents the graphical user interface of the game.
 */
public class GUI extends JFrame {
    private Spaceship spaceship; // The spaceship object
    public GUI() {
        spaceship = new Spaceship(); // Initialize the spaceship object
    }
    public void init() {
        // Set up the JFrame
        setTitle("Space Defender");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setResizable(false);
        // Set up the JPanel
        JPanel panel = new JPanel();
        panel.setPreferredSize(new Dimension(800, 600));
        panel.setFocusable(true);
        panel.requestFocusInWindow();
        panel.addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                handleKeyPress(e);
            }
        });
        // Add the panel to the JFrame
        add(panel);
        pack();
        setLocationRelativeTo(null);
        setVisible(true);
    }
    private void handleKeyPress(KeyEvent e) {
        int keyCode = e.getKeyCode();
        if (keyCode == KeyEvent.VK_LEFT) {
            moveSpaceshipLeft();
        } else if (keyCode == KeyEvent.VK_RIGHT) {
            moveSpaceshipRight();
        } else if (keyCode == KeyEvent.VK_UP) {
            moveSpaceshipUp();
        } else if (keyCode == KeyEvent.VK_DOWN) {
            moveSpaceshipDown();
        }
    }
    private void moveSpaceshipLeft() {
        spaceship.moveLeft();
    }
    private void moveSpaceshipRight() {
        spaceship.moveRight();
    }
    private void moveSpaceshipUp() {
        spaceship.moveUp();
    }
    private void moveSpaceshipDown() {
        spaceship.moveDown();
    }
}