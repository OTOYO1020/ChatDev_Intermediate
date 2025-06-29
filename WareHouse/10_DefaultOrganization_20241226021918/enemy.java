/**
 * This class represents the enemy character in the game.
 */
public class Enemy {
    private int health;
    public Enemy() {
        health = 50;
    }
    public int getHealth() {
        return health;
    }
    public void decreaseHealth(int amount) {
        health -= amount;
    }
    public void generateNewEnemy() {
        // Generate a new enemy with full health
        health = 50;
    }
}