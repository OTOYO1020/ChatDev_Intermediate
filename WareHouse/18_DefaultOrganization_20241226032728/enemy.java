/**
 * This class represents an enemy in Urban Rampage.
 * It handles enemy attributes and behavior.
 */
public class Enemy {
    private String name;
    private int health;
    private int strength;
    private int agility;
    public Enemy(String name, int health, int strength, int agility) {
        this.name = name;
        this.health = health;
        this.strength = strength;
        this.agility = agility;
    }
    public void move() {
        // TODO: Implement enemy movement logic
        System.out.println("Enemy is moving...");
    }
    public void attack() {
        // TODO: Implement enemy attack logic
        System.out.println("Enemy is attacking...");
    }
    public void takeDamage(int damage) {
        // TODO: Implement enemy damage logic
        System.out.println("Enemy is taking damage...");
    }
    public void die() {
        // TODO: Implement enemy death logic
        System.out.println("Enemy has died...");
    }
}