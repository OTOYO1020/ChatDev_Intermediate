import javax.swing.*;
import java.awt.*;
/**
 * This class represents the game canvas where the game is rendered.
 */
public class GameCanvas extends JPanel {
    private Game game;
    public GameCanvas() {
        setFocusable(true);
        requestFocus();
    }
    public void setGame(Game game) {
        this.game = game;
    }
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        // Draw game objects
        Graphics2D g2d = (Graphics2D) g.create();
        if (game != null) {
            game.render(g2d);
        }
        g2d.dispose();
    }
}