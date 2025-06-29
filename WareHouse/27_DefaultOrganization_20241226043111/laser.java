/**
 * This class represents a laser shot by the spaceship.
 */
public class Laser {
    private int x;
    private int y;
    public Laser(int x, int y) {
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
        y -= GUI.LASER_SPEED;
    }
    public boolean intersects(Rectangle rectangle) {
        return new Rectangle(x, y, GUI.LASER_WIDTH, GUI.LASER_HEIGHT).intersects(rectangle);
    }
}