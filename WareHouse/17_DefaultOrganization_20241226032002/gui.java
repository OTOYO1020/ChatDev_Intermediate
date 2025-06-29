/**
 * This class represents the graphical user interface of the application.
 * It creates the main window and handles user interactions.
 */
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class GUI {
    private JFrame frame;
    private JButton button;
    private Game game;
    public GUI(Game game) {
        this.game = game;
    }
    public void start() {
        frame = new JFrame("Virtual Ninja Warrior");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(800, 600);
        frame.setLayout(new BorderLayout());
        JPanel gamePanel = new JPanel();
        gamePanel.setLayout(new BorderLayout());
        gamePanel.add(game);
        frame.add(gamePanel, BorderLayout.CENTER);
        button = new JButton("Click Me");
        button.addActionListener(new ButtonClickListener());
        frame.add(button, BorderLayout.SOUTH);
        frame.setVisible(true);
    }
    private class ButtonClickListener implements ActionListener {
        public void actionPerformed(ActionEvent event) {
            game.showMessage("Button Clicked!");
        }
    }
}