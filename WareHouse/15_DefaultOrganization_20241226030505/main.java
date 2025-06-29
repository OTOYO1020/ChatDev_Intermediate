/**
 * This class represents the entry point of the application.
 * It creates instances of the GUI and Game classes and starts the game.
 */
import javax.swing.JFrame;
import java.awt.FlowLayout;
public class Main {
    public static void main(String[] args) {
        GUI gui = new GUI();
        gui.start();
        Game game = new Game();
        game.start();
    }
}