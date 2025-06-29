/**
 * This class represents the level in the game.
 */
public class Level {
    private int level;
    public Level() {
        level = 1;
    }
    public int getLevel() {
        return level;
    }
    public void levelUp() {
        level++;
    }
}