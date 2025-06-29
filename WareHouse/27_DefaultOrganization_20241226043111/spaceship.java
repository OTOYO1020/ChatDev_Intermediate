/**
 * This class represents the player-controlled spaceship.
 */
public class Spaceship {
    private static final int SPEED = 5;
    private static final int MAX_HEALTH = 3;
    private int x;
    private int y;
    private int health;
    private int powerUpCount;
    public Spaceship(int x, int y) {
        this.x = x;
        this.y = y;
        this.health = MAX_HEALTH;
        this.powerUpCount = 0;
    }
    public int getX() {
        return x;
    }
    public int getY() {
        return y;
    }
    public int getHealth() {
        return health;
    }
    public void decreaseHealth() {
        health--;
    }
    public void upgrade() {
        powerUpCount++;
    }
    public void downgrade() {
        powerUpCount--;
    }
    public void moveLeft() {
        if (x > 0) {
            x -= SPEED;
        }
    }
    public void moveRight() {
        if (x < GUI.WIDTH - GUI.SPACESHIP_WIDTH) {
            x += SPEED;
        }
    }
    public void update() {
        if (powerUpCount > 0) {
            // Apply power-up effects
        }
    }
    public boolean intersects(Rectangle rectangle) {
        return new Rectangle(x, y, GUI.SPACESHIP_WIDTH, GUI.SPACESHIP_HEIGHT).intersects(rectangle);
    }
}