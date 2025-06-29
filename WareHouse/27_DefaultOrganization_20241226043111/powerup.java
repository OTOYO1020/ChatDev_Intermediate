/**
 * This class represents a power-up that upgrades the spaceship.
 */
public class PowerUp {
    private int x;
    private int y;
    public PowerUp(int x, int y) {
        this.x = x;
        this.y = y;
    }
    public int getX() {
        return x;
    }
    public int getY() {
        return y;
    }
    public void update() {
        y += GUI.POWERUP_SPEED;
    }
    public boolean intersects(Rectangle rectangle) {
        return new Rectangle(x, y, GUI.POWERUP_WIDTH, GUI.POWERUP_HEIGHT).intersects(rectangle);
    }
}