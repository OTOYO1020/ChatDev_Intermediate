import java.util.ArrayList;
import java.util.List;
import java.time.format.DateTimeFormatter;
/**
 * This class represents a Meeting Scheduler application that streamlines the process of scheduling and managing meetings for organizations.
 */
public class MeetingScheduler {
    private List<Meeting> meetings;
    public MeetingScheduler() {
        meetings = new ArrayList<>();
    }
    public void createMeeting(Meeting meeting) {
        meetings.add(meeting);
        System.out.println("Meeting created: " + meeting);
    }
    public void updateMeeting(Meeting meeting) {
        // Update meeting details
        System.out.println("Meeting updated: " + meeting);
    }
    public void displayMeetings() {
        for (Meeting meeting : meetings) {
            System.out.println(meeting);
        }
    }
    public static void main(String[] args) {
        MeetingScheduler meetingScheduler = new MeetingScheduler();
        meetingScheduler.createMeeting(new Meeting("Meeting 1", "Room 1", "2022-01-01 10:00"));
        meetingScheduler.createMeeting(new Meeting("Meeting 2", "Room 2", "2022-01-02 14:00"));
        meetingScheduler.displayMeetings();
    }
}