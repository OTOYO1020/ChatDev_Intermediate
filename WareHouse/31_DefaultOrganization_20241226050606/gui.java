import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.Timer;
/**
 * This class represents the GUI of the board game companion application.
 */
public class GUI extends JFrame implements TimerCallback {
    private JButton turnButton;
    private JButton scoreButton;
    private JButton ruleButton;
    private JButton playerAidButton;
    private JButton timerButton;
    private int timerDuration;
    private JLabel timerLabel;
    private TimerExample gameTimer;
    /**
     * Constructs the GUI and initializes the buttons.
     */
    public GUI() {
        setTitle("Board Game Companion");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());
        turnButton = new JButton("Turn Tracking");
        scoreButton = new JButton("Scorekeeping");
        ruleButton = new JButton("Rule References");
        playerAidButton = new JButton("Interactive Player Aids");
        timerButton = new JButton("Customizable Timer");
        timerDuration = 0;
        timerLabel = new JLabel("Timer: " + timerDuration + " seconds");
        turnButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Implement turn tracking functionality
                System.out.println("Turn tracking functionality");
            }
        });
        scoreButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Implement scorekeeping functionality
                System.out.println("Scorekeeping functionality");
            }
        });
        ruleButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Implement rule references functionality
                System.out.println("Rule references functionality");
            }
        });
        playerAidButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Implement interactive player aids functionality
                System.out.println("Interactive player aids functionality");
            }
        });
        timerButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Implement customizable timer functionality
                if (gameTimer != null) {
                    gameTimer.start();
                }
            }
        });
        add(turnButton);
        add(scoreButton);
        add(ruleButton);
        add(playerAidButton);
        add(timerButton);
        add(timerLabel);
    }
    /**
     * Makes the GUI visible.
     */
    @Override
    public void setVisible(boolean visible) {
        super.setVisible(visible);
    }
    /**
     * Sets the timer duration.
     *
     * @param duration the duration in seconds
     */
    public void setTimerDuration(int duration) {
        timerDuration = duration;
        timerLabel.setText("Timer: " + timerDuration + " seconds");
        gameTimer = new TimerExample(duration, this);
    }
    /**
     * Starts the GUI.
     */
    public void start() {
        setVisible(true);
    }
    /**
     * Callback method invoked when the timer is finished.
     */
    public void onTimerFinished() {
        // Implement timer finished functionality
        System.out.println("Timer finished functionality");
    }
}