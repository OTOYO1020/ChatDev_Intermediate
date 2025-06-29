import java.awt.*;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.ArrayList;
import java.util.List;
/**
 * This class represents the player character in the game.
 * It handles the player's shooting and movement.
 */
public class Player {
    private static final int PLAYER_WIDTH = 50;
    private static final int PLAYER_HEIGHT = 50;
    private int x;
    private int y;
    private int health;
    private List<Bullet> bullets;
    private boolean leftKeyPressed;
    private boolean rightKeyPressed;
    public Player() {
        // Initialize player position and health
        x = 0;
        y = 0;
        health = 100;
        bullets = new ArrayList<>();
        leftKeyPressed = false;
        rightKeyPressed = false;
    }
    public void shoot() {
        Bullet bullet = new Bullet(x, y); // Create a new bullet at the player's position
        bullets.add(bullet);
    }
    public void update() {
        // Implement player movement logic
        // Update player position based on user input or AI
        if (leftKeyPressed) {
            x -= 1; // Move player left
        }
        if (rightKeyPressed) {
            x += 1; // Move player right
        }
    }
    public boolean isColliding(Enemy enemy) {
        // Implement collision detection logic between player and enemy
        Rectangle playerBounds = new Rectangle(x, y, PLAYER_WIDTH, PLAYER_HEIGHT);
        Rectangle enemyBounds = new Rectangle(enemy.getX(), enemy.getY(), Enemy.ENEMY_WIDTH, Enemy.ENEMY_HEIGHT);
        return playerBounds.intersects(enemyBounds);
    }
    public void decreaseHealth() {
        health -= 10;
    }
    public int getHealth() {
        return health;
    }
    public List<Bullet> getBullets() {
        return bullets;
    }
    public void setLeftKeyPressed(boolean leftKeyPressed) {
        this.leftKeyPressed = leftKeyPressed;
    }
    public void setRightKeyPressed(boolean rightKeyPressed) {
        this.rightKeyPressed = rightKeyPressed;
    }
}