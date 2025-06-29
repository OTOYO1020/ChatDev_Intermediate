import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the graphical user interface (GUI) for the application.
 * It creates a window with buttons and handles user interactions.
 */
public class GUI extends JFrame {
    private JButton startButton;
    private JButton quitButton;
    private Game game;
    public GUI() {
        setTitle("Arcane Arena");
        setSize(300, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());
        startButton = new JButton("Start Game");
        startButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Perform action when the start button is clicked
                handleStartButtonClick();
            }
        });
        add(startButton);
        quitButton = new JButton("Quit Game");
        quitButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Perform action when the quit button is clicked
                handleQuitButtonClick();
            }
        });
        add(quitButton);
    }
    public void start() {
        setVisible(true);
    }
    private void handleStartButtonClick() {
        game = new Game();
        game.start();
    }
    private void handleQuitButtonClick() {
        if (game != null) {
            game.endGame();
        }
        System.exit(0);
    }
}