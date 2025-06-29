'''
This file contains the Character class that represents a player character in the game.
'''
public class Character {
    private String name;
    private String playstyle;
    private int health;
    private int attack;
    private int defense;
    public Character(String name, String playstyle, int health, int attack, int defense) {
        this.name = name;
        this.playstyle = playstyle;
        this.health = health;
        this.attack = attack;
        this.defense = defense;
    }
    public String getName() {
        return name;
    }
    public String getPlaystyle() {
        return playstyle;
    }
    public int getHealth() {
        return health;
    }
    public int getAttack() {
        return attack;
    }
    public int getDefense() {
        return defense;
    }
    public void attack(Character target) {
        int damage = this.attack - target.getDefense();
        if (damage > 0) {
            target.takeDamage(damage);
        }
    }
    public void takeDamage(int damage) {
        this.health -= damage;
        if (this.health < 0) {
            this.health = 0;
        }
    }
}