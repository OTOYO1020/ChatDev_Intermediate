/**
 * This class represents the player character in the game.
 */
import javax.swing.JOptionPane;
public class Player {
    private int health;
    private int score;
    private boolean specialMoveAvailable;
    public Player() {
        health = 100;
        score = 0;
        specialMoveAvailable = true;
    }
    public int getHealth() {
        return health;
    }
    public int getScore() {
        return score;
    }
    public void decreaseHealth(int amount) {
        health -= amount;
    }
    public void increaseScore() {
        score++;
    }
    public void attack(Enemy enemy) {
        // Implement attack logic here
        enemy.decreaseHealth(10);
    }
    public void block() {
        // Implement block logic here
        // Reduce damage taken by the player
        // For example, you can decrease the health by a smaller amount when the player blocks
        health -= 5;
    }
    public void specialMove(Enemy enemy) {
        // Implement special move logic here
        // Perform a powerful attack with a cooldown
        if (specialMoveAvailable) {
            enemy.decreaseHealth(20);
            specialMoveAvailable = false;
            // Start a cooldown timer
            new Thread(() -> {
                try {
                    Thread.sleep(5000); // Cooldown time in milliseconds (5 seconds)
                    specialMoveAvailable = true;
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }).start();
        } else {
            JOptionPane.showMessageDialog(null, "Special move is on cooldown. Please wait.");
        }
    }
}