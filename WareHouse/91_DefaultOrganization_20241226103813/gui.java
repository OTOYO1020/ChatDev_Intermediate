import javax.swing.JPanel;
import javax.swing.JLabel;
import java.awt.Dimension;
/**
 * GUI class for the user interface
 */
public class GUI extends JPanel {
    public GUI() {
        // Set the preferred size of the panel
        setPreferredSize(new Dimension(800, 600));
        // Add components and configure layout
        add(new JLabel("Hello, World!"));
    }
}