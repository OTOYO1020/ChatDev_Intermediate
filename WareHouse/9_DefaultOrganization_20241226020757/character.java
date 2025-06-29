/**
 * This class represents a character in the game.
 */
public class Character {
    private String name;
    private int maxHealth;
    private List<Spell> spells;
    public Character(String name, int maxHealth) {
        this.name = name;
        this.maxHealth = maxHealth;
        this.spells = new ArrayList<>();
    }
    public String getName() {
        return name;
    }
    public int getMaxHealth() {
        return maxHealth;
    }
    public List<Spell> getSpells() {
        return spells;
    }
    public void addSpell(Spell spell) {
        spells.add(spell);
    }
}