/**
 * This class represents the industry average data and handles the input and retrieval of industry average data.
 */
public class IndustryAverageData {
    private double averageSale;
    /**
     * Set the average sale.
     *
     * @param averageSale The average sale to be set.
     * @throws IllegalArgumentException if the average sale is negative.
     */
    public void setAverageSale(double averageSale) {
        if (averageSale < 0) {
            throw new IllegalArgumentException("Average sale cannot be negative");
        }
        this.averageSale = averageSale;
    }
    /**
     * Get the average sale.
     *
     * @return The average sale.
     */
    public double getAverageSale() {
        return averageSale;
    }
}