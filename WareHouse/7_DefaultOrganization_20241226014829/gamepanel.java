import javax.swing.*;
import java.awt.*;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
/**
 * This class represents the game panel where the game is rendered.
 */
public class GamePanel extends JPanel {
    private Player player;
    private List<Bullet> bullets;
    private List<Enemy> enemies;
    private int score;
    public GamePanel() {
        // Set the panel size
        setPreferredSize(new Dimension(800, 600));
        // Create the player
        player = new Player(this);
        // Create the lists for bullets and enemies
        bullets = new ArrayList<>();
        enemies = new ArrayList<>();
        // Add key listener to handle player movement and shooting
        addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                player.handleKeyPress(e);
            }
            @Override
            public void keyReleased(KeyEvent e) {
                player.handleKeyRelease(e);
            }
        });
        setFocusable(true);
        requestFocus();
        score = 0;
    }
    public void update() {
        // Update the player
        player.update();
        // Update the bullets
        Iterator<Bullet> bulletIterator = bullets.iterator();
        while (bulletIterator.hasNext()) {
            Bullet bullet = bulletIterator.next();
            bullet.update();
            // Remove bullets that are out of bounds
            if (bullet.getX() > 800) {
                bulletIterator.remove();
            }
        }
        // Update the enemies
        Iterator<Enemy> enemyIterator = enemies.iterator();
        while (enemyIterator.hasNext()) {
            Enemy enemy = enemyIterator.next();
            enemy.update();
            // Remove enemies that are out of bounds
            if (enemy.getX() < -50) {
                enemyIterator.remove();
            }
        }
        // Check for collisions between bullets and enemies
        bulletIterator = bullets.iterator();
        while (bulletIterator.hasNext()) {
            Bullet bullet = bulletIterator.next();
            enemyIterator = enemies.iterator();
            while (enemyIterator.hasNext()) {
                Enemy enemy = enemyIterator.next();
                if (bullet.intersects(enemy)) {
                    // Remove the bullet and enemy from the lists
                    bulletIterator.remove();
                    enemyIterator.remove();
                    // Increase the player's score
                    increaseScore();
                    break;
                }
            }
        }
        // Check for collisions between player and enemies
        for (Enemy enemy : enemies) {
            if (player.intersects(enemy)) {
                // Game over condition
                player.gameOver();
                break;
            }
        }
    }
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        // Render the player
        player.render(g);
        // Render the bullets
        for (Bullet bullet : bullets) {
            bullet.render(g);
        }
        // Render the enemies
        for (Enemy enemy : enemies) {
            enemy.render(g);
        }
        // Render the player's score
        g.setColor(Color.WHITE);
        g.drawString("Score: " + score, 10, 20);
    }
    public void addEnemy(Enemy enemy) {
        enemies.add(enemy);
    }
    public void addBullet(Bullet bullet) {
        bullets.add(bullet);
    }
    public void handleKeyPress(KeyEvent e) {
        player.handleKeyPress(e);
    }
    public void handleKeyRelease(KeyEvent e) {
        player.handleKeyRelease(e);
    }
    @Override
    public void keyPressed(KeyEvent e) {
        handleKeyPress(e);
    }
    @Override
    public void keyReleased(KeyEvent e) {
        handleKeyRelease(e);
    }
    public void increaseScore() {
        score++;
    }
}