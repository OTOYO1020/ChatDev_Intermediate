import java.util.HashMap;
import java.util.Map;
/**
 * This class represents the Customer Acquisition Tracker application.
 * It provides features for recording and categorizing customer acquisition channels,
 * tracking the number of acquired customers through each channel,
 * and generating reports to analyze the effectiveness of different acquisition strategies.
 */
public class CustomerAcquisitionTracker {
    private Map<String, Integer> acquisitionChannels;
    public CustomerAcquisitionTracker() {
        acquisitionChannels = new HashMap<>();
    }
    /**
     * Records the acquisition of a customer through a specific channel.
     *
     * @param channel the acquisition channel
     */
    public void recordAcquisition(String channel) {
        if (acquisitionChannels.containsKey(channel)) {
            int count = acquisitionChannels.get(channel);
            acquisitionChannels.put(channel, count + 1);
        } else {
            acquisitionChannels.put(channel, 1);
        }
    }
    /**
     * Generates a report of the acquired customers for each channel.
     *
     * @return the report as a string
     */
    public String generateReport() {
        StringBuilder report = new StringBuilder();
        for (Map.Entry<String, Integer> entry : acquisitionChannels.entrySet()) {
            String channel = entry.getKey();
            int count = entry.getValue();
            report.append(channel).append(": ").append(count).append("\n");
        }
        return report.toString();
    }
}