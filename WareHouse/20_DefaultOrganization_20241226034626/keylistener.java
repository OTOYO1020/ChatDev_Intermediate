import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
/**
 * This class represents the key listener for player movement.
 */
public class GameKeyListener implements KeyListener {
    private Game game;
    public GameKeyListener(Game game) {
        this.game = game;
    }
    @Override
    public void keyTyped(KeyEvent e) {
        // Not used
    }
    @Override
    public void keyPressed(KeyEvent e) {
        // Handle key press event
    }
    @Override
    public void keyReleased(KeyEvent e) {
        // Handle key release event
    }
}