/**
 * This class represents the player character.
 */
public class Player {
    private int health;
    private Weapon weapon;
    private Ability ability;
    public Player() {
        health = 100;
    }
    /**
     * This method performs an attack on the enemy.
     *
     * @param enemy The enemy to attack.
     * @return The damage dealt by the attack.
     */
    public int attack(Enemy enemy) {
        // Check if the player has a weapon
        if (weapon != null) {
            int damageDealt = weapon.getDamage();
            enemy.takeDamage(damageDealt);
            return damageDealt;
        }
        return 0;
    }
    /**
     * This method sets the player's weapon.
     *
     * @param weapon The weapon to set.
     */
    public void setWeapon(Weapon weapon) {
        this.weapon = weapon;
    }
    /**
     * This method sets the player's ability.
     *
     * @param ability The ability to set.
     */
    public void setAbility(Ability ability) {
        this.ability = ability;
    }
    /**
     * This method gets the player's health.
     *
     * @return The player's health.
     */
    public int getHealth() {
        return health;
    }
    /**
     * This method reduces the player's health by the specified amount.
     *
     * @param damage The amount of damage to take.
     */
    public void takeDamage(int damage) {
        health -= damage;
    }
}