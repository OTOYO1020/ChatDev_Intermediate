import java.awt.*;
/**
 * This class represents the enemies in the game.
 */
public class Enemy {
    private int x;
    private int y;
    private int speed;
    public Enemy(int x, int y) {
        this.x = x;
        this.y = y;
        speed = 3;
    }
    public void update() {
        // Update enemy logic
        x -= speed;
    }
    public void render(Graphics g) {
        // Render enemy graphics
        g.setColor(Color.GREEN);
        g.fillRect(x, y, 50, 50);
    }
    public int getX() {
        return x;
    }
}