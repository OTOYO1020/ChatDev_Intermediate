/**
 * This class represents the game logic and graphical user interface (GUI) of the application.
 */
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JFrame;
import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class Game extends JPanel {
    private Player player;
    private Enemy enemy;
    private Level level;
    private JButton attackButton;
    private JButton blockButton;
    private JButton specialMoveButton;
    private JLabel playerHealthLabel;
    private JLabel enemyHealthLabel;
    public Game() {
        // Set up the main panel
        setLayout(new BorderLayout());
        // Create the player, enemy, and level
        player = new Player();
        enemy = new Enemy();
        level = new Level();
        // Create the buttons
        attackButton = new JButton("Attack");
        blockButton = new JButton("Block");
        specialMoveButton = new JButton("Special Move");
        // Create the labels
        playerHealthLabel = new JLabel("Player Health: " + player.getHealth());
        enemyHealthLabel = new JLabel("Enemy Health: " + enemy.getHealth());
        // Add the components to the panel
        JPanel buttonPanel = new JPanel();
        buttonPanel.add(attackButton);
        buttonPanel.add(blockButton);
        buttonPanel.add(specialMoveButton);
        add(buttonPanel, BorderLayout.SOUTH);
        add(playerHealthLabel, BorderLayout.WEST);
        add(enemyHealthLabel, BorderLayout.EAST);
        // Add action listeners to the buttons
        attackButton.addActionListener(new ButtonClickListener());
        blockButton.addActionListener(new ButtonClickListener());
        specialMoveButton.addActionListener(new ButtonClickListener());
    }
    /**
     * This method starts the game by making it visible.
     */
    public void start() {
        JFrame frame = new JFrame("Street Fighter");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().add(this);
        frame.pack();
        frame.setVisible(true);
    }
    /**
     * This class represents the action listener for the buttons.
     */
    private class ButtonClickListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            if (e.getSource() == attackButton) {
                player.attack(enemy);
            } else if (e.getSource() == blockButton) {
                player.block();
            } else if (e.getSource() == specialMoveButton) {
                player.specialMove(enemy);
            }
            // Update the health labels
            playerHealthLabel.setText("Player Health: " + player.getHealth());
            enemyHealthLabel.setText("Enemy Health: " + enemy.getHealth());
            // Check if the enemy is defeated
            if (enemy.getHealth() <= 0) {
                // Increase the player's score and level up
                player.increaseScore();
                level.levelUp();
                // Display a message to the player
                JOptionPane.showMessageDialog(Game.this, "Enemy defeated! Score: " + player.getScore() + ", Level: " + level.getLevel());
                // Generate a new enemy
                enemy.generateNewEnemy();
                enemyHealthLabel.setText("Enemy Health: " + enemy.getHealth());
            }
        }
    }
}