/**
 * This class represents the player in the game.
 * It contains properties and methods related to the player.
 */
public class Player extends GameObject {
    // Properties of the player
    private int health;
    private int score;
    // Constructor
    public Player(int health) {
        super(0, 0);
        this.health = health;
        this.score = 0;
    }
    // Method to update the player's score
    public void updateScore(int points) {
        score += points;
    }
    // Method to update the player's health
    public void updateHealth(int value) {
        health += value;
    }
    // Method to check if the player is colliding with another object
    @Override
    public boolean isColliding(GameObject object) {
        // Code to check collision
        Rectangle playerBounds = new Rectangle(getX(), getY(), getWidth(), getHeight());
        Rectangle objectBounds = new Rectangle(object.getX(), object.getY(), object.getWidth(), object.getHeight());
        return playerBounds.intersects(objectBounds);
    }
    // Method to update the player
    @Override
    public void update() {
        // Code to update the player's position based on user input
        setX(getX() + 1);
    }
}