/**
 * This class represents a ninja in the game.
 * Each ninja has unique abilities and weapons.
 */
public class Ninja {
    private String name;
    private int health;
    private int attackPower;
    private int defensePower;
    private String specialMove;
    public Ninja(String name, int health, int attackPower, int defensePower, String specialMove) {
        this.name = name;
        this.health = health;
        this.attackPower = attackPower;
        this.defensePower = defensePower;
        this.specialMove = specialMove;
    }
    public String getName() {
        return name;
    }
    public int getHealth() {
        return health;
    }
    public int getAttackPower() {
        return attackPower;
    }
    public int getDefensePower() {
        return defensePower;
    }
    public String getSpecialMove() {
        return specialMove;
    }
    public void attack(Ninja opponent) {
        int damage = attackPower - opponent.getDefensePower();
        opponent.takeDamage(damage);
    }
    public void takeDamage(int damage) {
        health -= damage;
        if (health < 0) {
            health = 0;
        }
    }
    public boolean isAlive() {
        return health > 0;
    }
}