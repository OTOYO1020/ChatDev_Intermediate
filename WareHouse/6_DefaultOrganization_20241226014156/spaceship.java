import java.awt.*;
import java.awt.event.KeyEvent;
/**
 * This class represents the spaceship controlled by the player.
 */
public class Spaceship {
    private int x; // x-coordinate of the spaceship
    private int y; // y-coordinate of the spaceship
    public Spaceship() {
        // Initialize the spaceship's position
        x = 0;
        y = 0;
    }
    public void moveLeft() {
        // Move the spaceship to the left
        x -= 1;
    }
    public void moveRight() {
        // Move the spaceship to the right
        x += 1;
    }
    public void moveUp() {
        // Move the spaceship up
        y -= 1;
    }
    public void moveDown() {
        // Move the spaceship down
        y += 1;
    }
    public int getX() {
        // Get the x-coordinate of the spaceship
        return x;
    }
    public int getY() {
        // Get the y-coordinate of the spaceship
        return y;
    }
}