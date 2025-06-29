import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the game logic of the application.
 * It handles the player, enemy forces, and game state.
 */
public class Game {
    private GUI gui;
    private Player player;
    private Enemy[] enemies;
    private Timer timer;
    public Game() {
        gui = new GUI(this);
        player = new Player();
        enemies = new Enemy[5]; // Adjust the number of enemies as needed
        for (int i = 0; i < enemies.length; i++) {
            enemies[i] = new Enemy();
        }
        timer = new Timer(1000 / 60, new TimerListener());
    }
    public void start() {
        gui.createAndShowGUI();
        timer.start();
    }
    public void shoot() {
        player.shoot();
    }
    public Player getPlayer() {
        return player;
    }
    private void update() {
        player.update();
        for (Enemy enemy : enemies) {
            enemy.update();
            if (player.isColliding(enemy)) {
                player.decreaseHealth();
                if (player.getHealth() <= 0) {
                    endGame();
                }
            }
        }
        for (Bullet bullet : player.getBullets()) {
            bullet.update();
            for (Enemy enemy : enemies) {
                if (bullet.isColliding(enemy)) {
                    enemy.remove();
                    bullet.remove();
                }
            }
        }
        gui.updateGUI(player, enemies);
    }
    private void endGame() {
        timer.stop();
        JOptionPane.showMessageDialog(null, "Game Over");
        System.exit(0);
    }
    private class TimerListener implements ActionListener {
        public void actionPerformed(ActionEvent event) {
            update();
        }
    }
}