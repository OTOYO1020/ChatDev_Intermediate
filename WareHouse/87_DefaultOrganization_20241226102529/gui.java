import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the graphical user interface (GUI) of the application.
 */
public class GUI extends JFrame {
    private JButton button;
    private JLabel label;
    public GUI() {
        setTitle("Application");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());
        button = new JButton("Click Me");
        label = new JLabel("Hello World!");
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                label.setText("Button Clicked");
            }
        });
        add(button);
        add(label);
    }
    /**
     * This method starts the GUI and makes it visible.
     */
    public void start() {
        EventQueue.invokeLater(new Runnable() {
            public void run() {
                setVisible(true);
            }
        });
    }
}