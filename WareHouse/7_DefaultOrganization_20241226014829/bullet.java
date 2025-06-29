import java.awt.*;
/**
 * This class represents the bullets fired by the player.
 */
public class Bullet {
    private int x;
    private int y;
    private int speed;
    public Bullet(int x, int y) {
        this.x = x;
        this.y = y;
        speed = 10;
    }
    public void update() {
        // Update bullet logic
        x += speed;
    }
    public void render(Graphics g) {
        // Render bullet graphics
        g.setColor(Color.YELLOW);
        g.fillOval(x, y, 10, 10);
    }
    public int getX() {
        return x;
    }
    public boolean intersects(Enemy enemy) {
        Rectangle bulletRect = new Rectangle(x, y, 10, 10);
        Rectangle enemyRect = new Rectangle(enemy.getX(), enemy.getY(), 50, 50);
        return bulletRect.intersects(enemyRect);
    }
}