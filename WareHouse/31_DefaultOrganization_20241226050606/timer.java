import java.util.Timer;
import java.util.TimerTask;
/**
 * This class represents a customizable timer for games.
 */
public class TimerExample {
    private Timer timer;
    private int seconds;
    private TimerCallback callback;
    /**
     * Constructs a TimerExample object with the specified number of seconds.
     *
     * @param seconds the number of seconds for the timer
     * @param callback the callback to be invoked when the timer is finished
     */
    public TimerExample(int seconds, TimerCallback callback) {
        this.seconds = seconds;
        this.callback = callback;
    }
    /**
     * Starts the timer.
     */
    public void start() {
        timer = new Timer();
        timer.scheduleAtFixedRate(new TimerTask() {
            public void run() {
                if (seconds == 0) {
                    timer.cancel();
                    callback.onTimerFinished();
                } else {
                    System.out.println("Seconds remaining: " + seconds);
                    seconds--;
                }
            }
        }, 0, 1000);
    }
}