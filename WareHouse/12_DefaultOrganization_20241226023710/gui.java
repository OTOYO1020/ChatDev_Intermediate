import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * GUI class for the Adrenaline Rush game.
 */
public class GUI extends JFrame {
    private JButton shootButton;
    private JButton abilityButton;
    private JLabel enemyHealthLabel; // Added enemy health label
    private JLabel playerHealthLabel; // Added player health label
    private JLabel playerScoreLabel; // Added player score label
    public GUI() {
        setTitle("Adrenaline Rush");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setResizable(false);
        setLayout(new BorderLayout());
        JPanel buttonPanel = new JPanel();
        buttonPanel.setLayout(new FlowLayout());
        shootButton = new JButton("Shoot");
        abilityButton = new JButton("Use Ability");
        buttonPanel.add(shootButton);
        buttonPanel.add(abilityButton);
        add(buttonPanel, BorderLayout.SOUTH);
        // Create enemy health label
        enemyHealthLabel = new JLabel("Enemy Health: 100");
        enemyHealthLabel.setHorizontalAlignment(SwingConstants.CENTER);
        add(enemyHealthLabel, BorderLayout.CENTER);
        // Create player health label
        playerHealthLabel = new JLabel("Player Health: 100");
        playerHealthLabel.setHorizontalAlignment(SwingConstants.CENTER);
        add(playerHealthLabel, BorderLayout.NORTH);
        // Create player score label
        playerScoreLabel = new JLabel("Player Score: 0");
        playerScoreLabel.setHorizontalAlignment(SwingConstants.CENTER);
        add(playerScoreLabel, BorderLayout.EAST);
        pack();
        setLocationRelativeTo(null);
        setVisible(true);
    }
    public void addShootButtonListener(ActionListener listener) {
        shootButton.addActionListener(listener);
    }
    public void addAbilityButtonListener(ActionListener listener) {
        abilityButton.addActionListener(listener);
    }
    public void updateEnemyHealth(int health) {
        enemyHealthLabel.setText("Enemy Health: " + health);
    }
    public void updatePlayerHealth(int health) {
        playerHealthLabel.setText("Player Health: " + health);
    }
    public void updatePlayerScore(int score) {
        playerScoreLabel.setText("Player Score: " + score);
    }
}