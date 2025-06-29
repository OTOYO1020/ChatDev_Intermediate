import java.util.ArrayList;
import java.util.List;
import SalesData;
/**
 * This class is responsible for analyzing the sales data.
 */
public class SalesDataAnalyzer {
    private List<SalesData> salesData;
    public SalesDataAnalyzer() {
        // Initialize the sales data
        salesData = new ArrayList<>();
        salesData.add(new SalesData("Product A", 10, 100.0));
        salesData.add(new SalesData("Product B", 5, 200.0));
        salesData.add(new SalesData("Product C", 8, 150.0));
    }
    public List<SalesData> getSalesData() {
        return salesData;
    }
    /**
     * Calculates the total revenue from the sales data.
     *
     * @return the total revenue
     */
    public double calculateTotalRevenue() {
        double totalRevenue = 0;
        for (SalesData data : salesData) {
            totalRevenue += data.getQuantity() * data.getPrice();
        }
        return totalRevenue;
    }
    /**
     * Calculates the average quantity from the sales data.
     *
     * @return the average quantity
     */
    public double calculateAverageQuantity() {
        int totalQuantity = 0;
        for (SalesData data : salesData) {
            totalQuantity += data.getQuantity();
        }
        return (double) totalQuantity / salesData.size();
    }
    /**
     * Identifies the best selling product from the sales data.
     *
     * @return the name of the best selling product
     */
    public String identifyBestSellingProduct() {
        String bestSellingProduct = "";
        int maxQuantity = 0;
        for (SalesData data : salesData) {
            if (data.getQuantity() > maxQuantity) {
                maxQuantity = data.getQuantity();
                bestSellingProduct = data.getProductName();
            }
        }
        return bestSellingProduct;
    }
}