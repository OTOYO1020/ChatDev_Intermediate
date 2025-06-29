import java.awt.*;
import java.awt.event.KeyEvent;
/**
 * This class represents the player in the game.
 */
public class Player {
    private int x;
    private int y;
    private int speed;
    private boolean gameOver;
    private Direction direction;
    private GamePanel gamePanel;
    public Player(GamePanel gamePanel) {
        x = 400;
        y = 300;
        speed = 5;
        gameOver = false;
        direction = Direction.NONE;
        this.gamePanel = gamePanel;
    }
    public void handleKeyPress(KeyEvent e) {
        int keyCode = e.getKeyCode();
        if (keyCode == KeyEvent.VK_UP) {
            direction = Direction.UP;
        } else if (keyCode == KeyEvent.VK_DOWN) {
            direction = Direction.DOWN;
        } else if (keyCode == KeyEvent.VK_LEFT) {
            direction = Direction.LEFT;
        } else if (keyCode == KeyEvent.VK_RIGHT) {
            direction = Direction.RIGHT;
        } else if (keyCode == KeyEvent.VK_SPACE) {
            shoot();
        }
    }
    public void handleKeyRelease(KeyEvent e) {
        int keyCode = e.getKeyCode();
        if (keyCode == KeyEvent.VK_UP && direction == Direction.UP) {
            direction = Direction.NONE;
        } else if (keyCode == KeyEvent.VK_DOWN && direction == Direction.DOWN) {
            direction = Direction.NONE;
        } else if (keyCode == KeyEvent.VK_LEFT && direction == Direction.LEFT) {
            direction = Direction.NONE;
        } else if (keyCode == KeyEvent.VK_RIGHT && direction == Direction.RIGHT) {
            direction = Direction.NONE;
        }
    }
    public void update() {
        // Update player logic
        if (gameOver) {
            return;
        }
        // Move the player based on the current direction
        if (direction == Direction.UP) {
            y -= speed;
        } else if (direction == Direction.DOWN) {
            y += speed;
        } else if (direction == Direction.LEFT) {
            x -= speed;
        } else if (direction == Direction.RIGHT) {
            x += speed;
        }
        // Keep the player within the game panel bounds
        if (x < 0) {
            x = 0;
        } else if (x > 750) {
            x = 750;
        }
        if (y < 0) {
            y = 0;
        } else if (y > 550) {
            y = 550;
        }
    }
    public void render(Graphics g) {
        // Render player graphics
        g.setColor(Color.RED);
        g.fillRect(x, y, 50, 50);
    }
    public boolean intersects(Enemy enemy) {
        Rectangle playerRect = new Rectangle(x, y, 50, 50);
        Rectangle enemyRect = new Rectangle(enemy.getX(), enemy.getY(), 50, 50);
        return playerRect.intersects(enemyRect);
    }
    public void gameOver() {
        gameOver = true;
    }
    private void shoot() {
        int bulletX = x + 50;
        int bulletY = y + 25;
        Bullet bullet = new Bullet(bulletX, bulletY);
        gamePanel.addBullet(bullet);
    }
    private enum Direction {
        NONE, UP, DOWN, LEFT, RIGHT
    }
}