/**
 * This class represents the GUI for the timer assistant application.
 * It provides methods for controlling the timer, setting the timer duration, enabling/disabling countdown display, and setting sound alerts.
 */
import java.io.IOException;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.sound.sampled.LineUnavailableException;
import javax.sound.sampled.UnsupportedAudioFileException;
import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Timer;
import java.util.TimerTask;
import javax.swing.JPanel;
public class GUI {
    private Timer timer;
    private int duration;
    private boolean countdownDisplayEnabled;
    private String soundAlert;
    /**
     * Pause the timer.
     */
    public void pauseTimer() {
        if (timer != null) {
            timer.cancel();
        }
    }
    /**
     * Resume the timer.
     */
    public void resumeTimer() {
        if (duration > 0) {
            startTimer(duration);
        }
    }
    /**
     * Set the timer duration for a specific game phase or turn.
     *
     * @param duration The duration of the timer in seconds.
     */
    public void setTimerDuration(int duration) {
        this.duration = duration;
    }
    /**
     * Enable or disable the countdown display.
     *
     * @param enable True to enable countdown display, false to disable.
     */
    public void enableCountdownDisplay(boolean enable) {
        countdownDisplayEnabled = enable;
    }
    /**
     * Set the sound alert for the timer.
     *
     * @param sound The sound alert to be played.
     */
    public void setSoundAlert(String sound) {
        soundAlert = sound;
    }
    /**
     * Start the timer with the specified duration.
     *
     * @param duration The duration of the timer in seconds.
     */
    private void startTimer(int duration) {
        timer = new Timer(true);
        timer.schedule(new TimerTask() {
            int remainingTime = duration;
            @Override
            public void run() {
                if (countdownDisplayEnabled) {
                    System.out.println("Time remaining: " + remainingTime);
                }
                if (remainingTime == 0) {
                    playSoundAlert();
                    timer.cancel();
                }
                remainingTime--;
            }
        }, 0, 1000);
    }
    /**
     * Play the sound alert.
     */
    private void playSoundAlert() {
        try {
            AudioInputStream audioInputStream = AudioSystem.getAudioInputStream(getClass().getResource(soundAlert));
            Clip clip = AudioSystem.getClip();
            clip.open(audioInputStream);
            clip.start();
        } catch (UnsupportedAudioFileException | IOException | LineUnavailableException e) {
            e.printStackTrace();
        }
    }
    /**
     * Start the timer assistant application.
     */
    public void start() {
        // Create and configure the main window
        JFrame mainWindow = new JFrame("Timer Assistant");
        mainWindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        mainWindow.setSize(400, 300);
        // Create and configure the UI components (e.g., buttons, labels, etc.)
        JButton startButton = new JButton("Start");
        JButton pauseButton = new JButton("Pause");
        JButton resumeButton = new JButton("Resume");
        // Add event listeners to the buttons to handle user interactions
        startButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Start the timer with the specified duration
                startTimer(duration);
            }
        });
        pauseButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Pause the timer
                pauseTimer();
            }
        });
        resumeButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Resume the timer
                resumeTimer();
            }
        });
        // Add the UI components to the main window
        JPanel mainPanel = new JPanel();
        mainPanel.add(startButton);
        mainPanel.add(pauseButton);
        mainPanel.add(resumeButton);
        mainWindow.add(mainPanel);
        // Display the main window
        mainWindow.setVisible(true);
    }
}