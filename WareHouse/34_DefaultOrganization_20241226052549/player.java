/**
 * This class represents a player in the game.
 * Each player has a name and a score.
 */
public class Player {
    private String name;
    private int points;
    public Player(String name) {
        this.name = name;
        this.points = 0;
    }
    public String getName() {
        return name;
    }
    public int getPoints() {
        return points;
    }
    public void addPoints(int points) {
        this.points += points;
    }
}