import java.util.Map;
/**
 * This class generates reports based on the inventory and stock orders.
 */
public class ReportGenerator {
    private Inventory inventory;
    private StockOrder stockOrder;
    public ReportGenerator(Inventory inventory, StockOrder stockOrder) {
        this.inventory = inventory;
        this.stockOrder = stockOrder;
    }
    /**
     * Generate a report of the inventory levels.
     *
     * @return the report as a string
     */
    public String generateInventoryReport() {
        StringBuilder report = new StringBuilder();
        report.append("Inventory Report:\n");
        for (Map.Entry<String, Integer> entry : inventory.getItems().entrySet()) {
            String itemName = entry.getKey();
            int quantity = entry.getValue();
            report.append(itemName).append(": ").append(quantity).append("\n");
        }
        return report.toString();
    }
    /**
     * Generate a report of the stock order history.
     *
     * @return the report as a string
     */
    public String generateStockOrderHistoryReport() {
        StringBuilder report = new StringBuilder();
        report.append("Stock Order History Report:\n");
        for (Map.Entry<String, Integer> entry : stockOrder.getItems().entrySet()) {
            String itemName = entry.getKey();
            int quantity = entry.getValue();
            report.append(itemName).append(": ").append(quantity).append("\n");
        }
        return report.toString();
    }
}