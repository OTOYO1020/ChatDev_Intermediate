import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;
/**
 * This class represents the GUI of the dice tower application.
 */
public class GUI extends JFrame {
    private JButton rollButton;
    private JTextArea resultTextArea;
    private DiceTower diceTower;
    /**
     * Constructor to initialize the GUI components.
     */
    public GUI() {
        setTitle("Dice Tower");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());
        // Create the roll button
        rollButton = new JButton("Roll");
        rollButton.addActionListener(new RollButtonListener());
        // Create the result text area
        resultTextArea = new JTextArea();
        resultTextArea.setEditable(false);
        // Add the components to the frame
        add(rollButton, BorderLayout.NORTH);
        add(resultTextArea, BorderLayout.CENTER);
        // Create a new dice tower
        diceTower = new DiceTower();
    }
    /**
     * Method to start the GUI.
     */
    public void start() {
        pack();
        setVisible(true);
    }
    /**
     * ActionListener for the roll button.
     */
    private class RollButtonListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            // Roll the dice and update the result text area
            int result = diceTower.rollDice();
            resultTextArea.setText("Result: " + result);
        }
    }
}
/**
 * This class represents the dice tower.
 */
public class DiceTower {
    private Random random;
    /**
     * Constructor to initialize the dice tower.
     */
    public DiceTower() {
        random = new Random();
    }
    /**
     * Method to roll the dice.
     *
     * @return the result of the dice roll.
     */
    public int rollDice() {
        // Generate a random number between 1 and 6
        int result = random.nextInt(6) + 1;
        return result;
    }
}