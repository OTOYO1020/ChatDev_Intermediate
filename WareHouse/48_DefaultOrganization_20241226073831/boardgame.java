/**
 * This class represents a board game scenario.
 * It allows players to create and share their own challenging scenarios.
 */
public class BoardGame {
    private String boardSetup;
    private String missions;
    private int resourceLimitations;
    private String victoryConditions;
    private int numberOfPlayers;
    private int difficultyLevel;
    public BoardGame(String boardSetup, String missions, int resourceLimitations, String victoryConditions, int numberOfPlayers, int difficultyLevel) {
        this.boardSetup = boardSetup;
        this.missions = missions;
        this.resourceLimitations = resourceLimitations;
        this.victoryConditions = victoryConditions;
        this.numberOfPlayers = numberOfPlayers;
        this.difficultyLevel = difficultyLevel;
    }
    public String getBoardSetup() {
        return boardSetup;
    }
    public void setBoardSetup(String boardSetup) {
        this.boardSetup = boardSetup;
    }
    public String getMissions() {
        return missions;
    }
    public void setMissions(String missions) {
        this.missions = missions;
    }
    public int getResourceLimitations() {
        return resourceLimitations;
    }
    public void setResourceLimitations(int resourceLimitations) {
        this.resourceLimitations = resourceLimitations;
    }
    public String getVictoryConditions() {
        return victoryConditions;
    }
    public void setVictoryConditions(String victoryConditions) {
        this.victoryConditions = victoryConditions;
    }
    public int getNumberOfPlayers() {
        return numberOfPlayers;
    }
    public void setNumberOfPlayers(int numberOfPlayers) {
        this.numberOfPlayers = numberOfPlayers;
    }
    public int getDifficultyLevel() {
        return difficultyLevel;
    }
    public void setDifficultyLevel(int difficultyLevel) {
        this.difficultyLevel = difficultyLevel;
    }
}