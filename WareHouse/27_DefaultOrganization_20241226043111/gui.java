import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Timer;
import java.util.TimerTask;
/**
 * This class represents the graphical user interface (GUI) of the application.
 * It contains the main window and handles user interactions.
 */
public class GUI extends JFrame implements KeyListener, ActionListener {
    private static final int WIDTH = 800;
    private static final int HEIGHT = 600;
    private static final int SPACESHIP_WIDTH = 50;
    private static final int SPACESHIP_HEIGHT = 50;
    private static final int LASER_WIDTH = 10;
    private static final int LASER_HEIGHT = 20;
    private static final int ENEMY_WIDTH = 50;
    private static final int ENEMY_HEIGHT = 50;
    private static final int POWERUP_WIDTH = 30;
    private static final int POWERUP_HEIGHT = 30;
    private static final int OBSTACLE_WIDTH = 100;
    private static final int OBSTACLE_HEIGHT = 20;
    private static final int LASER_SPEED = 5;
    private static final int ENEMY_SPEED = 2;
    private static final int POWERUP_SPEED = 2;
    private static final int OBSTACLE_SPEED = 1;
    private static final int POWERUP_DURATION = 5000;
    private static final int MAX_ENEMIES = 5;
    private static final int MAX_OBSTACLES = 3;
    private static final int MAX_LEVEL = 5;
    private static final int SCORE_INCREMENT = 10;
    private Spaceship spaceship;
    private List<Laser> lasers;
    private List<EnemySpaceship> enemies;
    private List<PowerUp> powerUps;
    private List<Obstacle> obstacles;
    private int score;
    private int level;
    private Timer enemyTimer;
    private Timer powerUpTimer;
    private Timer obstacleTimer;
    private Timer gameLoopTimer;
    public GUI() {
        // Set up the main window
        setTitle("Action Game");
        setSize(WIDTH, HEIGHT);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(null);
        setResizable(false);
        addKeyListener(this);
        setFocusable(true);
        // Initialize game objects
        spaceship = new Spaceship(WIDTH / 2 - SPACESHIP_WIDTH / 2, HEIGHT - SPACESHIP_HEIGHT - 10);
        lasers = new ArrayList<>();
        enemies = new ArrayList<>();
        powerUps = new ArrayList<>();
        obstacles = new ArrayList<>();
        score = 0;
        level = 1;
        // Create the spaceship label
        JLabel spaceshipLabel = new JLabel();
        spaceshipLabel.setBounds(spaceship.getX(), spaceship.getY(), SPACESHIP_WIDTH, SPACESHIP_HEIGHT);
        spaceshipLabel.setIcon(new ImageIcon("spaceship.png"));
        add(spaceshipLabel);
        // Create the score label
        JLabel scoreLabel = new JLabel("Score: " + score);
        scoreLabel.setBounds(10, 10, 100, 20);
        add(scoreLabel);
        // Create the level label
        JLabel levelLabel = new JLabel("Level: " + level);
        levelLabel.setBounds(10, 40, 100, 20);
        add(levelLabel);
        // Create the start button
        JButton startButton = new JButton("Start");
        startButton.setBounds(WIDTH / 2 - 50, HEIGHT / 2 - 25, 100, 50);
        startButton.addActionListener(this);
        add(startButton);
        // Start the enemy timer
        enemyTimer = new Timer();
        enemyTimer.schedule(new EnemyTask(), 0, 1000);
        // Start the power-up timer
        powerUpTimer = new Timer();
        powerUpTimer.schedule(new PowerUpTask(), 0, 5000);
        // Start the obstacle timer
        obstacleTimer = new Timer();
        obstacleTimer.schedule(new ObstacleTask(), 0, 3000);
        // Start the game loop timer
        gameLoopTimer = new Timer();
        gameLoopTimer.schedule(new GameLoop(), 0, 16); // 16 milliseconds for approximately 60 frames per second
    }
    public void start() {
        // Make the main window visible
        setVisible(true);
    }
    @Override
    public void actionPerformed(ActionEvent e) {
        // Handle button click events
        String actionCommand = e.getActionCommand();
        if (actionCommand.equals("Start")) {
            // Remove the start button
            getContentPane().removeAll();
            revalidate();
            repaint();
            // Set focus to the main window
            setFocusable(true);
            requestFocus();
        }
    }
    @Override
    public void keyPressed(KeyEvent e) {
        int keyCode = e.getKeyCode();
        if (keyCode == KeyEvent.VK_LEFT) {
            spaceship.moveLeft();
        } else if (keyCode == KeyEvent.VK_RIGHT) {
            spaceship.moveRight();
        } else if (keyCode == KeyEvent.VK_SPACE) {
            lasers.add(new Laser(spaceship.getX() + SPACESHIP_WIDTH / 2 - LASER_WIDTH / 2, spaceship.getY()));
        }
    }
    @Override
    public void keyReleased(KeyEvent e) {
        // Do nothing
    }
    @Override
    public void keyTyped(KeyEvent e) {
        // Do nothing
    }
    private class EnemyTask extends TimerTask {
        @Override
        public void run() {
            if (enemies.size() < MAX_ENEMIES) {
                Random random = new Random();
                int x = random.nextInt(WIDTH - ENEMY_WIDTH);
                int y = -ENEMY_HEIGHT;
                enemies.add(new EnemySpaceship(x, y));
            }
        }
    }
    private class PowerUpTask extends TimerTask {
        @Override
        public void run() {
            Random random = new Random();
            int x = random.nextInt(WIDTH - POWERUP_WIDTH);
            int y = -POWERUP_HEIGHT;
            powerUps.add(new PowerUp(x, y));
        }
    }
    private class ObstacleTask extends TimerTask {
        @Override
        public void run() {
            if (obstacles.size() < MAX_OBSTACLES) {
                Random random = new Random();
                int x = random.nextInt(WIDTH - OBSTACLE_WIDTH);
                int y = -OBSTACLE_HEIGHT;
                obstacles.add(new Obstacle(x, y));
            }
        }
    }
    private class GameLoop extends TimerTask {
        @Override
        public void run() {
            // Update spaceship position
            spaceship.update();
            // Update laser positions
            for (Laser laser : lasers) {
                laser.update();
            }
            // Update enemy positions
            for (EnemySpaceship enemy : enemies) {
                enemy.update();
            }
            // Update power-up positions
            for (PowerUp powerUp : powerUps) {
                powerUp.update();
            }
            // Update obstacle positions
            for (Obstacle obstacle : obstacles) {
                obstacle.update();
            }
            // Check for collisions
            checkCollisions();
            // Repaint the GUI
            repaint();
        }
    }
    private void checkCollisions() {
        // Check for collision between lasers and enemies
        for (Laser laser : lasers) {
            for (EnemySpaceship enemy : enemies) {
                if (laser.intersects(enemy)) {
                    lasers.remove(laser);
                    enemies.remove(enemy);
                    score += SCORE_INCREMENT;
                    break;
                }
            }
        }
        // Check for collision between spaceship and enemies
        for (EnemySpaceship enemy : enemies) {
            if (spaceship.intersects(enemy)) {
                enemies.remove(enemy);
                spaceship.decreaseHealth();
                if (spaceship.getHealth() <= 0) {
                    gameOver();
                }
                break;
            }
        }
        // Check for collision between spaceship and power-ups
        for (PowerUp powerUp : powerUps) {
            if (spaceship.intersects(powerUp)) {
                powerUps.remove(powerUp);
                spaceship.upgrade();
                Timer powerUpTimer = new Timer();
                powerUpTimer.schedule(new TimerTask() {
                    @Override
                    public void run() {
                        spaceship.downgrade();
                    }
                }, POWERUP_DURATION);
                break;
            }
        }
        // Check for collision between spaceship and obstacles
        for (Obstacle obstacle : obstacles) {
            if (spaceship.intersects(obstacle)) {
                obstacles.remove(obstacle);
                spaceship.decreaseHealth();
                if (spaceship.getHealth() <= 0) {
                    gameOver();
                }
                break;
            }
        }
    }
    private void gameOver() {
        enemyTimer.cancel();
        powerUpTimer.cancel();
        obstacleTimer.cancel();
        gameLoopTimer.cancel();
        JOptionPane.showMessageDialog(null, "Game Over! Your score: " + score);
        System.exit(0);
    }
    @Override
    public void paint(Graphics g) {
        super.paint(g);
        // Draw spaceship
        g.drawImage(new ImageIcon("spaceship.png").getImage(), spaceship.getX(), spaceship.getY(), SPACESHIP_WIDTH, SPACESHIP_HEIGHT, null);
        // Draw lasers
        for (Laser laser : lasers) {
            g.setColor(Color.RED);
            g.fillRect(laser.getX(), laser.getY(), LASER_WIDTH, LASER_HEIGHT);
        }
        // Draw enemies
        for (EnemySpaceship enemy : enemies) {
            g.drawImage(new ImageIcon("enemy.png").getImage(), enemy.getX(), enemy.getY(), ENEMY_WIDTH, ENEMY_HEIGHT, null);
        }
        // Draw power-ups
        for (PowerUp powerUp : powerUps) {
            g.drawImage(new ImageIcon("powerup.png").getImage(), powerUp.getX(), powerUp.getY(), POWERUP_WIDTH, POWERUP_HEIGHT, null);
        }
        // Draw obstacles
        for (Obstacle obstacle : obstacles) {
            g.setColor(Color.GRAY);
            g.fillRect(obstacle.getX(), obstacle.getY(), OBSTACLE_WIDTH, OBSTACLE_HEIGHT);
        }
    }
}