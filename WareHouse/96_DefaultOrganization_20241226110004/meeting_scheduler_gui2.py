import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
public class MeetingSchedulerGUI2 extends Application {
    private MeetingScheduler meetingScheduler;
    @Override
    public void start(Stage primaryStage) {
        meetingScheduler = new MeetingScheduler();
        primaryStage.setTitle("Meeting Scheduler");
        Button createButton = new Button("Create Meeting");
        createButton.setOnAction(e -> createMeeting());
        Button displayButton = new Button("Display Meetings");
        displayButton.setOnAction(e -> displayMeetings());
        VBox layout = new VBox(10);
        layout.getChildren().addAll(createButton, displayButton);
        Scene scene = new Scene(layout, 300, 200);
        primaryStage.setScene(scene);
        primaryStage.show();
    }
    private void createMeeting() {
        // Show a dialog to input meeting details
        Meeting meeting = new Meeting("Meeting 3", "Room 3", "2022-01-03 16:00");
        meetingScheduler.createMeeting(meeting);
    }
    private void displayMeetings() {
        meetingScheduler.displayMeetings();
    }
    public static void main(String[] args) {
        launch(args);
    }
}