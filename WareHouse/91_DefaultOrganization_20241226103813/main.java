/**
 * Main class to initialize and launch the GUI
 */
import javax.swing.JFrame;
public class Main {
    public static void main(String[] args) {
        GUI gui = new GUI();
        JFrame frame = new JFrame("Business Analytics");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().add(gui);
        frame.pack();
        frame.setVisible(true);
    }
}