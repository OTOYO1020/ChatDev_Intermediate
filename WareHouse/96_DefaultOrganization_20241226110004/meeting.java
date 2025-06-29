import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
/**
 * This class represents a meeting with its details.
 */
public class Meeting {
    private String title;
    private String location;
    private LocalDateTime dateTime;
    public Meeting(String title, String location, String dateTime) {
        this.title = title;
        this.location = location;
        this.dateTime = LocalDateTime.parse(dateTime, DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm"));
    }
    // Getters and setters
    @Override
    public String toString() {
        return "Meeting{" +
                "title='" + title + '\'' +
                ", location='" + location + '\'' +
                ", dateTime=" + dateTime +
                '}';
    }
}