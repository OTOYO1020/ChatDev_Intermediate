import java.util.List;
import com.example.Player;
import com.example.Resource;
import com.example.Objective;
public class GameState {
    private List<Player> players;
    private List<Resource> resources;
    private List<Objective> objectives;
    // Default constructor
    public GameState() {
    }
    // Constructor
    public GameState(List<Player> players, List<Resource> resources, List<Objective> objectives) {
        this.players = players;
        this.resources = resources;
        this.objectives = objectives;
    }
    // Getters and setters
    public List<Player> getPlayers() {
        return players;
    }
    public void setPlayers(List<Player> players) {
        this.players = players;
    }
    public List<Resource> getResources() {
        return resources;
    }
    public void setResources(List<Resource> resources) {
        this.resources = resources;
    }
    public List<Objective> getObjectives() {
        return objectives;
    }
    public void setObjectives(List<Objective> objectives) {
        this.objectives = objectives;
    }
}