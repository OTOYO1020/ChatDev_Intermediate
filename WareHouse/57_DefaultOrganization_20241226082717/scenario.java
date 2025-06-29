/**
 * This class represents a board game scenario.
 */
public class Scenario {
    private String boardSetup;
    private String objectives;
    private String missions;
    private String victoryConditions;
    private String obstacles;
    private String bonuses;
    public Scenario(String boardSetup, String objectives, String missions, String victoryConditions, String obstacles, String bonuses) {
        this.boardSetup = boardSetup;
        this.objectives = objectives;
        this.missions = missions;
        this.victoryConditions = victoryConditions;
        this.obstacles = obstacles;
        this.bonuses = bonuses;
    }
    // Getters and setters for the scenario properties
    public String getBoardSetup() {
        return boardSetup;
    }
    public void setBoardSetup(String boardSetup) {
        this.boardSetup = boardSetup;
    }
    public String getObjectives() {
        return objectives;
    }
    public void setObjectives(String objectives) {
        this.objectives = objectives;
    }
    public String getMissions() {
        return missions;
    }
    public void setMissions(String missions) {
        this.missions = missions;
    }
    public String getVictoryConditions() {
        return victoryConditions;
    }
    public void setVictoryConditions(String victoryConditions) {
        this.victoryConditions = victoryConditions;
    }
    public String getObstacles() {
        return obstacles;
    }
    public void setObstacles(String obstacles) {
        this.obstacles = obstacles;
    }
    public String getBonuses() {
        return bonuses;
    }
    public void setBonuses(String bonuses) {
        this.bonuses = bonuses;
    }
    @Override
    public String toString() {
        return "Scenario{" +
                "boardSetup='" + boardSetup + '\'' +
                ", objectives='" + objectives + '\'' +
                ", missions='" + missions + '\'' +
                ", victoryConditions='" + victoryConditions + '\'' +
                ", obstacles='" + obstacles + '\'' +
                ", bonuses='" + bonuses + '\'' +
                '}';
    }
}