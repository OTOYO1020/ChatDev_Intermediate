import javax.swing.JFrame;
import GUI;
public class main {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Ninja Assassin");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(800, 600);
        frame.setLocationRelativeTo(null);
        GUI gui = new GUI();
        frame.add(gui);
        frame.setVisible(true);
    }
}