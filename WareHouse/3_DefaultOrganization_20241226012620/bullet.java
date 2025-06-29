/**
 * This class represents the bullets fired by the player.
 * It handles bullet movement and collision detection.
 */
public class Bullet {
    private static final int BULLET_WIDTH = 10;
    private static final int BULLET_HEIGHT = 10;
    private int x;
    private int y;
    public Bullet(int x, int y) {
        this.x = x;
        this.y = y;
    }
    public void update() {
        // Implement bullet movement logic
        // Update bullet position based on game rules
        y -= 1; // Move bullet up
    }
    public boolean isColliding(Enemy enemy) {
        // Implement collision detection logic between bullet and enemy
        Rectangle bulletBounds = new Rectangle(x, y, BULLET_WIDTH, BULLET_HEIGHT);
        Rectangle enemyBounds = new Rectangle(enemy.getX(), enemy.getY(), Enemy.ENEMY_WIDTH, Enemy.ENEMY_HEIGHT);
        return bulletBounds.intersects(enemyBounds);
    }
    public void remove() {
        // Implement logic to remove the bullet from the game
    }
}