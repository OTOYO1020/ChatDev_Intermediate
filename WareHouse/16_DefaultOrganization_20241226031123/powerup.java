/**
 * This class represents a power-up in the game.
 * It contains properties and methods related to power-ups.
 */
public class PowerUp extends GameObject {
    // Properties of a power-up
    private String type;
    // Constructor
    public PowerUp(String type) {
        super(0, 0);
        this.type = type;
    }
    // Method to apply the power-up effect
    public void applyEffect(Player player) {
        // Code to apply power-up effect
        if (type.equals("Health")) {
            player.updateHealth(10);
        }
    }
    // Method to update the power-up
    @Override
    public void update() {
        // Code to update the power-up's position based on its effect
        setY(getY() + 1);
    }
}