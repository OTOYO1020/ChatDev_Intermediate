/**
 * This class represents an enemy ship in the game.
 * It contains properties and methods related to enemy ships.
 */
public class EnemyShip extends GameObject {
    // Properties of an enemy ship
    private int health;
    private int speed;
    // Constructor
    public EnemyShip(int health, int speed) {
        super(0, 0);
        this.health = health;
        this.speed = speed;
    }
    // Method to destroy the enemy ship
    public void destroy() {
        // Code to destroy the enemy ship
        health = 0;
    }
    // Method to check if the enemy ship is colliding with another object
    @Override
    public boolean isColliding(GameObject object) {
        // Code to check collision
        Rectangle enemyShipBounds = new Rectangle(getX(), getY(), getWidth(), getHeight());
        Rectangle objectBounds = new Rectangle(object.getX(), object.getY(), object.getWidth(), object.getHeight());
        return enemyShipBounds.intersects(objectBounds);
    }
    // Method to update the enemy ship
    @Override
    public void update() {
        // Code to update the enemy ship's position based on its speed
        setX(getX() + speed);
    }
}