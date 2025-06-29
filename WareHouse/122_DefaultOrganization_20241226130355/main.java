'''
This is the main class that starts the application.
'''
import javax.swing.SwingUtilities;
public class Main {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            GUI gui = new GUI();
            gui.createAndShowGUI();
        });
    }
}