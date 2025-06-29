import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.HashMap;
import java.util.Map;
/**
 * This class represents the graphical user interface of the application.
 * It creates the main window and handles user interactions.
 */
public class GUI {
    private JFrame frame;
    private Game game;
    private JLabel healthLabel;
    private Map<Integer, Boolean> keyStates;
    public GUI(Game game) {
        this.game = game;
        keyStates = new HashMap<>();
    }
    public void createAndShowGUI() {
        frame = new JFrame("Action Game");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        JButton button = new JButton("Shoot");
        button.addActionListener(new ButtonClickListener());
        frame.getContentPane().setLayout(new FlowLayout());
        frame.getContentPane().add(button);
        healthLabel = new JLabel("Health: 100");
        frame.getContentPane().add(healthLabel);
        frame.setVisible(true);
        frame.addKeyListener(new KeyListener() {
            @Override
            public void keyTyped(KeyEvent e) {
                // Empty implementation
            }
            @Override
            public void keyPressed(KeyEvent e) {
                keyStates.put(e.getKeyCode(), true);
                handlePlayerMovement();
            }
            @Override
            public void keyReleased(KeyEvent e) {
                keyStates.put(e.getKeyCode(), false);
                handlePlayerMovement();
            }
        });
        frame.setFocusable(true);
        frame.requestFocus();
    }
    public void updateGUI(Player player, Enemy[] enemies) {
        healthLabel.setText("Health: " + player.getHealth());
        frame.repaint();
    }
    private void handlePlayerMovement() {
        boolean leftKeyPressed = keyStates.getOrDefault(KeyEvent.VK_LEFT, false);
        boolean rightKeyPressed = keyStates.getOrDefault(KeyEvent.VK_RIGHT, false);
        game.getPlayer().setLeftKeyPressed(leftKeyPressed);
        game.getPlayer().setRightKeyPressed(rightKeyPressed);
    }
    private class ButtonClickListener implements ActionListener {
        public void actionPerformed(ActionEvent event) {
            game.shoot();
        }
    }
}