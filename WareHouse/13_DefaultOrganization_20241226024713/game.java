import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the game logic of the application.
 */
public class GameLogic {
    private Player player;
    private Enemy enemy;
    private Timer enemyTimer;
    private GUI gui;
    private int defeatedEnemies;
    public GameLogic() {
        // Initialize player and enemy instances
        player = new Player();
        enemy = new Enemy();
        // Set the player's weapon and ability
        Weapon playerWeapon = new Weapon(10); // Example weapon with damage 10
        player.setWeapon(playerWeapon);
        Ability playerAbility = new Ability("Double Attack"); // Example ability with name "Double Attack"
        player.setAbility(playerAbility);
        // Create a timer for enemy AI actions
        enemyTimer = new Timer(1000, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                performEnemyAction();
            }
        });
        defeatedEnemies = 0;
    }
    /**
     * This method starts the game by starting the enemy timer.
     */
    public void start() {
        // Create and start the GUI
        gui = new GUI(this);
        gui.start();
        // Start the enemy timer
        enemyTimer.start();
    }
    /**
     * This method performs the player action.
     */
    public void performPlayerAction() {
        // Check if player and enemy instances exist
        if (player == null || enemy == null) {
            return;
        }
        // Perform player attack
        int damageDealt = player.attack(enemy);
        // Update labels with battle results
        gui.getLabel().setText("Player Health: " + player.getHealth() + " | Enemy Health: " + enemy.getHealth() + " | Damage Dealt: " + damageDealt);
        // Check if the enemy is defeated
        if (enemy.getHealth() <= 0) {
            // Stop the enemy timer
            enemyTimer.stop();
            // Increment defeated enemies count
            defeatedEnemies++;
            // Unlock new weapons and abilities
            unlockNewWeaponsAndAbilities();
        }
    }
    /**
     * This method performs the enemy AI action.
     */
    private void performEnemyAction() {
        // Check if player and enemy instances exist
        if (player == null || enemy == null) {
            return;
        }
        // Perform enemy attack
        enemy.attack(player);
        // Update labels with battle results
        gui.getLabel().setText("Player Health: " + player.getHealth() + " | Enemy Health: " + enemy.getHealth());
        // Check if the player is defeated
        if (player.getHealth() <= 0) {
            // Stop the enemy timer
            enemyTimer.stop();
            // Game over logic
            gameOver();
        }
    }
    /**
     * This method unlocks new weapons and abilities for the player based on their progress.
     */
    private void unlockNewWeaponsAndAbilities() {
        if (defeatedEnemies >= 10) {
            // Unlock new weapons and abilities
            Weapon newWeapon = new Weapon(15); // Example new weapon with damage 15
            player.setWeapon(newWeapon);
            Ability newAbility = new Ability("Healing"); // Example new ability with name "Healing"
            player.setAbility(newAbility);
        }
    }
    /**
     * This method handles the game over logic.
     */
    private void gameOver() {
        // Display a game over message
        JOptionPane.showMessageDialog(null, "Game Over");
        // Exit the application
        System.exit(0);
    }
    /**
     * This method returns the player's health.
     *
     * @return The player's health.
     */
    public int getPlayerHealth() {
        return player.getHealth();
    }
    /**
     * This method returns the enemy's health.
     *
     * @return The enemy's health.
     */
    public int getEnemyHealth() {
        return enemy.getHealth();
    }
}