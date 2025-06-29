import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;
import BoardGameStrategyCoach.*;
/**
 * This class represents the application and handles the GUI initialization and event handling.
 */
public class Application {
    private JFrame frame;
    private BoardGameStrategyCoach coach;
    public void start() {
        SwingUtilities.invokeLater(() -> {
            createAndShowGUI();
        });
    }
    private void createAndShowGUI() {
        frame = new JFrame("Board Game Strategy Coach");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Create and add GUI components here
        coach = new BoardGameStrategyCoach();
        frame.add(coach.getGUIComponent());
        frame.pack();
        frame.setVisible(true);
    }
}