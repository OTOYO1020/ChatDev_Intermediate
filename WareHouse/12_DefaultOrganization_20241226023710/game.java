import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JOptionPane;
import javax.swing.Timer;
/**
 * Game class for the Adrenaline Rush game.
 */
public class Game {
    private GUI gui;
    private Player player;
    private Enemy enemy;
    private int wave; // New attribute to track the current wave number
    public Game() {
        gui = new GUI();
        player = new Player();
        enemy = new Enemy();
        wave = 1; // Start from wave 1
    }
    public void start() {
        // Check if player's health is zero or below
        if (player.getHealth() <= 0) {
            // Stop the game and display a message to the player
            JOptionPane.showMessageDialog(gui, "Game Over! You have lost.", "Game Over", JOptionPane.INFORMATION_MESSAGE);
            return;
        }
        while (wave <= 3) { // Assuming there are 3 waves in the game
            // Display the current wave number to the player
            JOptionPane.showMessageDialog(gui, "Wave " + wave, "Wave", JOptionPane.INFORMATION_MESSAGE);
            // Game logic for each wave goes here
            wave++; // Move to the next wave
        }
        // Display a message to the player indicating that they have completed all waves and won the game
        JOptionPane.showMessageDialog(gui, "Congratulations! You have completed all waves and won the game.", "Game Over", JOptionPane.INFORMATION_MESSAGE);
        // Update the GUI with the player's final score
        gui.updatePlayerScore(player.getScore());
    }
}