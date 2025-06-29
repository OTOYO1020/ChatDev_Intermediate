/**
 * This class represents a board game.
 * It contains the game name, scoring rules, and a list of players.
 */
import java.util.ArrayList;
import java.util.List;
public class Game {
    private String name;
    private String scoringRules;
    private List<Player> players;
    public Game(String name, String scoringRules) {
        this.name = name;
        this.scoringRules = scoringRules;
        this.players = new ArrayList<>();
    }
    public String getName() {
        return name;
    }
    public String getScoringRules() {
        return scoringRules;
    }
    public List<Player> getPlayers() {
        return players;
    }
    public void addPlayer(String playerName) {
        players.add(new Player(playerName));
    }
    public void recordScore(String playerName, int score) {
        for (Player player : players) {
            if (player.getName().equals(playerName)) {
                player.setScore(score);
                break;
            }
        }
    }
}