import java.util.HashMap;
import java.util.Map;
/**
 * This class represents a stock order and manages its items.
 */
public class StockOrder {
    private Map<String, Integer> items;
    public StockOrder() {
        items = new HashMap<>();
    }
    /**
     * Add an item to the stock order.
     *
     * @param itemName the name of the item
     * @param quantity the quantity of the item
     */
    public void addItem(String itemName, int quantity) {
        items.put(itemName, quantity);
    }
    /**
     * Remove an item from the stock order.
     *
     * @param itemName the name of the item
     */
    public void removeItem(String itemName) {
        items.remove(itemName);
    }
    /**
     * Update the quantity of an item in the stock order.
     *
     * @param itemName the name of the item
     * @param quantity the new quantity of the item
     * @throws IllegalArgumentException if the item does not exist in the stock order
     */
    public void updateItemQuantity(String itemName, int quantity) {
        if (items.containsKey(itemName)) {
            items.put(itemName, quantity);
        } else {
            throw new IllegalArgumentException("Item does not exist in the stock order: " + itemName);
        }
    }
    /**
     * Get the quantity of an item in the stock order.
     *
     * @param itemName the name of the item
     * @return the quantity of the item
     */
    public int getItemQuantity(String itemName) {
        return items.getOrDefault(itemName, 0);
    }
    /**
     * Get all items in the stock order.
     *
     * @return the map of items
     */
    public Map<String, Integer> getItems() {
        return items;
    }
}