import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the game logic of the action game.
 * It handles the game state, player movement, and collision detection.
 */
public class Game {
    private GameCanvas gameCanvas;
    private JLabel scoreLabel;
    private Player player;
    private int score;
    public Game(GameCanvas gameCanvas, JLabel scoreLabel) {
        this.gameCanvas = gameCanvas;
        this.scoreLabel = scoreLabel;
        this.player = new Player();
        this.score = 0;
    }
    public void start() {
        // Start the game loop
        Timer timer = new Timer(16, new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                update();
                render();
            }
        });
        timer.start();
    }
    private void update() {
        // Update game state
        player.update();
        // Check for collision with obstacles or zombies
        if (checkCollision()) {
            gameOver();
        }
    }
    private void render() {
        // Clear the game canvas
        Graphics2D g2d = (Graphics2D) gameCanvas.getGraphics();
        g2d.clearRect(0, 0, gameCanvas.getWidth(), gameCanvas.getHeight());
        // Draw player
        player.draw(g2d);
        // Repaint the canvas
        gameCanvas.repaint();
    }
    public void movePlayer() {
        // Move the player
        player.move();
    }
    private boolean checkCollision() {
        // Check for collision with obstacles or zombies
        // Return true if collision occurs, false otherwise
        return false;
    }
    private void gameOver() {
        // Game over logic
        JOptionPane.showMessageDialog(gameCanvas, "Game Over!");
        System.exit(0);
    }
}