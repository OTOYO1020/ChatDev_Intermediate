/**
 * This class represents a spell in the game.
 */
public class Spell {
    private String name;
    private int damage;
    private int cooldown;
    public Spell(String name, int damage, int cooldown) {
        this.name = name;
        this.damage = damage;
        this.cooldown = cooldown;
    }
    public String getName() {
        return name;
    }
    public int getDamage() {
        return damage;
    }
    public int getCooldown() {
        return cooldown;
    }
}