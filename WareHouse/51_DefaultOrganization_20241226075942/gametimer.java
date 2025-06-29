import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Timer;
import java.util.TimerTask;
/**
 * This class represents the timer for the board game turn.
 * It allows players to set a specific time limit for each turn and displays a countdown timer during gameplay.
 * When the time is up, the software automatically moves to the next player.
 */
public class GameTimer {
    private int timeLimit;
    private int remainingSeconds;
    private Timer timer;
    private TimerTask timerTask;
    private JLabel label;
    private int currentPlayer;
    private ActionListener actionListener;
    /**
     * Constructs a GameTimer object with the specified time limit and label.
     *
     * @param timeLimit The time limit for each turn in seconds.
     * @param label     The label to display the countdown timer.
     */
    public GameTimer(int timeLimit, JLabel label) {
        this.timeLimit = timeLimit;
        this.remainingSeconds = timeLimit;
        this.label = label;
        this.currentPlayer = 1;
        this.actionListener = new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                updateTimer();
            }
        };
    }
    /**
     * Starts the timer.
     */
    public void start() {
        timer = new Timer();
        timerTask = new TimerTask() {
            @Override
            public void run() {
                SwingUtilities.invokeLater(actionListener);
            }
        };
        timer.scheduleAtFixedRate(timerTask, 0, 1000);
    }
    /**
     * Stops the timer.
     */
    public void stop() {
        timer.cancel();
    }
    /**
     * Updates the timer and moves to the next player if the time is up.
     */
    private void updateTimer() {
        label.setText("Time remaining: " + remainingSeconds + " seconds");
        remainingSeconds--;
        if (remainingSeconds < 0) {
            switchPlayer();
            stop();
        }
    }
    /**
     * Switches to the next player and updates the label to display the current player.
     */
    private void switchPlayer() {
        currentPlayer = currentPlayer == 1 ? 2 : 1;
        label.setText("Player " + currentPlayer + "'s turn");
    }
}