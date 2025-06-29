'''
This is the main file of the application. It contains the entry point for the program and initializes the GUI.
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