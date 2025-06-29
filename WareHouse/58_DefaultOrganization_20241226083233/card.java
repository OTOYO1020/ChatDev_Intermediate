/**
 * This class represents a card in the collection.
 */
public class Card {
    private String name;
    private int quantity;
    private String condition;
    public Card(String name, int quantity, String condition) {
        this.name = name;
        this.quantity = quantity;
        this.condition = condition;
    }
    public String getName() {
        return name;
    }
    public int getQuantity() {
        return quantity;
    }
    public String getCondition() {
        return condition;
    }
}