/**
 * This class manages the board game events.
 */
import java.util.ArrayList;
import java.util.List;
public class EventManager {
    private List<Event> events;
    public EventManager() {
        events = new ArrayList<>();
    }
    public void addEvent(Event event) {
        events.add(event);
    }
    public void removeEvent(Event event) {
        events.remove(event);
    }
    public List<Event> getEvents() {
        return events;
    }
}