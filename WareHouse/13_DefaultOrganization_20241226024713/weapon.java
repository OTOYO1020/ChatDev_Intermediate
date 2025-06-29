/**
 * This class represents a weapon.
 */
public class Weapon {
    private int damage;
    public Weapon(int damage) {
        this.damage = damage;
    }
    /**
     * This method gets the damage of the weapon.
     *
     * @return The damage of the weapon.
     */
    public int getDamage() {
        return damage;
    }
}