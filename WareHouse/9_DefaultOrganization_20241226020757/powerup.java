/**
 * This class represents a power-up in the game.
 */
public class PowerUp {
    private String name;
    private int duration;
    public PowerUp(String name, int duration) {
        this.name = name;
        this.duration = duration;
    }
    public String getName() {
        return name;
    }
    public int getDuration() {
        return duration;
    }
}