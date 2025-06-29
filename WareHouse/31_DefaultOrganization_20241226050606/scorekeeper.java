/**
 * This class represents a score keeper for games.
 */
public class ScoreKeeper {
    private int score;
    /**
     * Constructs a ScoreKeeper object with an initial score of 0.
     */
    public ScoreKeeper() {
        score = 0;
    }
    /**
     * Increments the score by 1.
     */
    public void incrementScore() {
        score++;
    }
    /**
     * Decrements the score by 1.
     */
    public void decrementScore() {
        score--;
    }
    /**
     * Returns the current score.
     *
     * @return the current score
     */
    public int getScore() {
        return score;
    }
}