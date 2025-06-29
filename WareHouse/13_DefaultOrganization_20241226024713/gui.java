import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the graphical user interface of the application.
 */
public class GUI extends JFrame implements ActionListener {
    private JButton button;
    private JLabel label;
    private GameLogic gameLogic;
    public GUI(GameLogic gameLogic) {
        this.gameLogic = gameLogic;
        // Set the title of the window
        setTitle("My Application");
        // Set the size of the window
        setSize(400, 300);
        // Set the layout manager
        setLayout(new FlowLayout());
        // Create the button
        button = new JButton("Click Me");
        // Create the label
        label = new JLabel("Hello World!");
        // Add the button and label to the window
        add(button);
        add(label);
        // Add action listener to the button
        button.addActionListener(this);
        // Set the default close operation
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
    /**
     * This method starts the GUI by making it visible.
     */
    public void start() {
        setVisible(true);
        // Update the label with initial health values
        label.setText("Player Health: " + gameLogic.getPlayerHealth() + " | Enemy Health: " + gameLogic.getEnemyHealth());
    }
    /**
     * This method returns the label of the GUI.
     *
     * @return The label of the GUI.
     */
    public JLabel getLabel() {
        return label;
    }
    @Override
    public void actionPerformed(ActionEvent e) {
        // Update the label text when the button is clicked
        label.setText("Button Clicked!");
        // Perform player action
        gameLogic.performPlayerAction();
    }
}