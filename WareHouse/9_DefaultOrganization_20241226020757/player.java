/**
 * This class represents a player in the game.
 */
public class Player {
    private String name;
    private Character character;
    private int health;
    private Position position;
    public Player(String name, Character character) {
        this.name = name;
        this.character = character;
        this.health = character.getMaxHealth();
        this.position = new Position(0, 0); // Set initial position
    }
    public String getName() {
        return name;
    }
    public Character getCharacter() {
        return character;
    }
    public int getHealth() {
        return health;
    }
    public void takeDamage(int damage) {
        health -= damage;
        if (health <= 0) {
            // Player is eliminated
        }
    }
    public void updatePosition() {
        // TODO: Implement player position update logic
        // Update the player's position based on their movement
    }
    public void castSpell() {
        // TODO: Implement spellcasting logic
        // Allow the player to cast spells based on their abilities
    }
    public Position getPosition() {
        return position;
    }
}