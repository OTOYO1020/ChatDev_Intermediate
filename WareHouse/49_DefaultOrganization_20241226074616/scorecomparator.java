/**
 * This class handles the score comparison logic.
 */
public class ScoreComparator {
    /**
     * This method compares the scores and returns the comparison result as a string.
     * @param scores1 The first array of scores.
     * @param scores2 The second array of scores.
     * @return The comparison result as a string.
     */
    public String compareScores(int[] scores1, int[] scores2) {
        int totalScore1 = calculateTotalScore(scores1);
        int totalScore2 = calculateTotalScore(scores2);
        if (totalScore1 > totalScore2) {
            return "Player 1 has a higher score";
        } else if (totalScore1 < totalScore2) {
            return "Player 2 has a higher score";
        } else {
            return "Both players have the same score";
        }
    }
    /**
     * This method calculates the total score from an array of scores.
     * @param scores The array of scores.
     * @return The total score.
     */
    private int calculateTotalScore(int[] scores) {
        int totalScore = 0;
        for (int score : scores) {
            totalScore += score;
        }
        return totalScore;
    }
}