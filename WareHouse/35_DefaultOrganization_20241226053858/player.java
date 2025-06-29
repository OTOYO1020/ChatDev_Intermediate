/**
 * This class represents a player in a board game.
 * It contains the player name and score.
 */
public class Player {
    private String name;
    private int score;
    public Player(String name) {
        this.name = name;
        this.score = 0;
    }
    public String getName() {
        return name;
    }
    public int getScore() {
        return score;
    }
    public void setScore(int score) {
        this.score = score;
    }
}