import javax.swing.JFrame;
import javax.swing.JPanel;
public class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Dice Tower");
        DiceTower diceTower = new DiceTower();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(new GUI(diceTower));
        frame.pack();
        frame.setVisible(true);
    }
}