/**
 * Enemy class for the Adrenaline Rush game.
 */
public class Enemy {
    private int health;
    private int damage;
    public Enemy() {
        health = 100;
        damage = 10;
    }
    public int getHealth() {
        return health;
    }
    public void setHealth(int health) {
        this.health = health;
    }
    public int getDamage() {
        return damage;
    }
    public void setDamage(int damage) {
        this.damage = damage;
    }
    public void decreaseHealth(int amount) {
        health -= amount;
    }
    // Add any additional methods or attributes as needed
}