/**
 * This class represents the AI opponent.
 */
public class Enemy {
    private int health;
    private Weapon weapon;
    public Enemy() {
        health = 100;
    }
    /**
     * This method performs an attack on the player.
     *
     * @param player The player to attack.
     */
    public void attack(Player player) {
        // Check if the enemy has a weapon
        if (weapon != null) {
            player.takeDamage(weapon.getDamage());
        }
    }
    /**
     * This method sets the enemy's weapon.
     *
     * @param weapon The weapon to set.
     */
    public void setWeapon(Weapon weapon) {
        this.weapon = weapon;
    }
    /**
     * This method reduces the enemy's health by the specified amount.
     *
     * @param damage The amount of damage to take.
     */
    public void takeDamage(int damage) {
        health -= damage;
    }
    /**
     * This method gets the enemy's health.
     *
     * @return The enemy's health.
     */
    public int getHealth() {
        return health;
    }
}