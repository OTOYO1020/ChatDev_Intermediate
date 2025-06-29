/**
 * This class represents an enemy spaceship.
 */
public class EnemySpaceship {
    private int x;
    private int y;
    public EnemySpaceship(int x, int y) {
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
        y += GUI.ENEMY_SPEED;
    }
    public boolean intersects(Rectangle rectangle) {
        return new Rectangle(x, y, GUI.ENEMY_WIDTH, GUI.ENEMY_HEIGHT).intersects(rectangle);
    }
}