import java.util.ArrayList;
import java.util.List;
/**
 * This class represents the data source for board game strategies.
 */
public class StrategyData {
    /**
     * This method returns a list of predefined board game strategies.
     */
    public static List<Strategy> getStrategies() {
        List<Strategy> strategies = new ArrayList<>();
        // Add strategies to the list
        strategies.add(new Strategy("Strategy 1", 0.75));
        strategies.add(new Strategy("Strategy 2", 0.65));
        strategies.add(new Strategy("Strategy 3", 0.80));
        return strategies;
    }
}