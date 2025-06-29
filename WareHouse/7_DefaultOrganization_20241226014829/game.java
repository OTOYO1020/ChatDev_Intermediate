import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the game logic and manages the game loop.
 */
public class GameLogic {
    private GamePanel gamePanel;
    private Timer enemyTimer;
    public GameLogic() {
        // Create the game panel
        gamePanel = new GamePanel();
    }
    public void start() {
        // Create the main window
        JFrame frame = new JFrame("Fast Shooter Game");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(800, 600);
        // Add the game panel to the main window
        frame.getContentPane().add(gamePanel, BorderLayout.CENTER);
        // Display the main window
        frame.setVisible(true);
        // Add a new enemy to the game panel at a fixed interval
        enemyTimer = new Timer(2000, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Add a new enemy to the game panel
                gamePanel.addEnemy(new Enemy(800, (int) (Math.random() * 550)));
            }
        });
        enemyTimer.start();
        // Start the game loop
        gameLoop();
    }
    private void gameLoop() {
        while (true) {
            // Update the game logic
            update();
            // Render the game graphics
            gamePanel.repaint();
            // Delay for a short period to control the game speed
            try {
                Thread.sleep(10);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
    private void update() {
        // Update the game panel
        gamePanel.update();
    }
}