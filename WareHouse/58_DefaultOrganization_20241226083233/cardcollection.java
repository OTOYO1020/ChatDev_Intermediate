import java.util.ArrayList;
import java.util.Iterator;
/**
 * This class represents a collection of cards.
 */
public class CardCollection {
    private ArrayList<Card> cardCollection;
    public CardCollection() {
        cardCollection = new ArrayList<>();
    }
    public void addCard(Card card) {
        cardCollection.add(card);
    }
    public void removeCard(String name) {
        Iterator<Card> iterator = cardCollection.iterator();
        while (iterator.hasNext()) {
            Card card = iterator.next();
            if (card.getName().equals(name)) {
                iterator.remove();
                break;
            }
        }
    }
    public Card searchCard(String name) {
        for (Card card : cardCollection) {
            if (card.getName().equals(name)) {
                return card;
            }
        }
        return null;
    }
    public ArrayList<Card> getCardCollection() {
        return cardCollection;
    }
}