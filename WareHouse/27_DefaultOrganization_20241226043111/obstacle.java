/**
 * This class represents an obstacle in the game.
 */
public class Obstacle {
    private int x;
    private int y;
    public Obstacle(int x, int y) {
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
        y += GUI.OBSTACLE_SPEED;
    }
    public boolean intersects(Rectangle rectangle) {
        return new Rectangle(x, y, GUI.OBSTACLE_WIDTH, GUI.OBSTACLE_HEIGHT).intersects(rectangle);
    }
}