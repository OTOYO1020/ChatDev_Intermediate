/**
 * This class represents a weapon in Urban Rampage.
 * It handles weapon attributes and behavior.
 */
public class Weapon {
    private String name;
    private int damage;
    private int durability;
    public Weapon(String name, int damage, int durability) {
        this.name = name;
        this.damage = damage;
        this.durability = durability;
    }
    public void attack() {
        // TODO: Implement weapon attack logic
        System.out.println("Weapon is attacking...");
    }
    public void repair() {
        // TODO: Implement weapon repair logic
        System.out.println("Weapon is being repaired...");
    }
}