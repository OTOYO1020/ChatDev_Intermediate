import javax.swing.JFrame;
import javax.swing.JButton;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JOptionPane;
import Game;
public class GUI extends JFrame {
    private JButton startButton;
    private JButton exitButton;
    public GUI() {
        setTitle("Ninja Assassin");
        setSize(800, 600);
        setLayout(null);
        startButton = new JButton("Start");
        startButton.setBounds(350, 250, 100, 50);
        startButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                startGame();
            }
        });
        add(startButton);
        exitButton = new JButton("Exit");
        exitButton.setBounds(350, 350, 100, 50);
        exitButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                exitGame();
            }
        });
        add(exitButton);
    }
    private void startGame() {
        Game game = new Game();
        game.start();
    }
    private void exitGame() {
        int option = JOptionPane.showConfirmDialog(this, "Are you sure you want to exit?", "Exit", JOptionPane.YES_NO_OPTION);
        if (option == JOptionPane.YES_OPTION) {
            System.exit(0);
        }
    }
}