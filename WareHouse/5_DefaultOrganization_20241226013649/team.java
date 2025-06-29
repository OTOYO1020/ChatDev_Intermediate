import java.util.ArrayList;
import java.util.List;
/**
 * This class represents a team of warriors.
 */
public class Team {
    private List<Warrior> warriors;
    public Team() {
        warriors = new ArrayList<>();
    }
    public void addWarrior(Warrior warrior) {
        warriors.add(warrior);
    }
    public void removeWarrior(Warrior warrior) {
        warriors.remove(warrior);
    }
    // Add other methods as needed
}