import java.util.HashMap;
import java.util.Map;
/**
 * This class represents the inventory and manages its items.
 */
public class Inventory {
    private Map<String, Integer> items;
    public Inventory() {
        items = new HashMap<>();
    }
    /**
     * Add an item to the inventory.
     *
     * @param itemName the name of the item
     * @param quantity the quantity of the item
     */
    public void addItem(String itemName, int quantity) {
        items.put(itemName, quantity);
    }
    /**
     * Remove an item from the inventory.
     *
     * @param itemName the name of the item
     */
    public void removeItem(String itemName) {
        items.remove(itemName);
    }
    /**
     * Update the quantity of an item in the inventory.
     *
     * @param itemName the name of the item
     * @param quantity the new quantity of the item
     */
    public void updateItemQuantity(String itemName, int quantity) {
        items.put(itemName, quantity);
    }
    /**
     * Get the quantity of an item in the inventory.
     *
     * @param itemName the name of the item
     * @return the quantity of the item
     */
    public int getItemQuantity(String itemName) {
        return items.getOrDefault(itemName, 0);
    }
    /**
     * Get all items in the inventory.
     *
     * @return the map of items
     */
    public Map<String, Integer> getItems() {
        return items;
    }
}