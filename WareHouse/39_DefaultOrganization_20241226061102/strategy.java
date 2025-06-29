/**
 * This class represents a board game strategy.
 */
public class Strategy {
    private String name;
    private double successRate;
    public Strategy(String name, double successRate) {
        this.name = name;
        this.successRate = successRate;
    }
    public String getName() {
        return name;
    }
    public double getSuccessRate() {
        return successRate;
    }
}