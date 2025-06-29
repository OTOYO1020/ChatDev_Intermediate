/**
 * Player class for the Adrenaline Rush game.
 */
public class Player {
    private int health;
    private int score;
    private int damage; // Added damage attribute
    private Weapon weapon;
    public Player() {
        health = 100;
        score = 0;
        damage = 20; // Set initial damage to 20
        weapon = new Weapon("Pistol", damage);
    }
    public int getHealth() {
        return health;
    }
    public void setHealth(int health) {
        this.health = health;
    }
    public int getScore() {
        return score;
    }
    public void setScore(int score) {
        this.score = score;
    }
    public int getDamage() {
        return damage;
    }
    public void setDamage(int damage) {
        this.damage = damage;
    }
    public Weapon getWeapon() {
        return weapon;
    }
    public void setWeapon(Weapon weapon) {
        this.weapon = weapon;
    }
    public void increaseScore(int points) {
        score += points;
    }
    public void increaseHealth(int amount) {
        health += amount;
    }
    public void increaseDamage(int amount) {
        damage += amount;
    }
    public void decreaseHealth(int amount) {
        health -= amount;
    }
    // Add any additional methods or attributes as needed
}