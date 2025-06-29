import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the game logic and graphical user interface of the application.
 */
public class Game extends JPanel {
    private JButton button;
    private JLabel label;
    public Game() {
        // Set up the main frame
        setPreferredSize(new Dimension(300, 200));
        setLayout(new FlowLayout());
        // Create the button
        button = new JButton("Click Me");
        button.addActionListener(new ButtonClickListener());
        // Create the label
        label = new JLabel("Hello, Monster Hunter!");
        // Add the components to the panel
        add(button);
        add(label);
    }
    /**
     * This method starts the game.
     */
    public void start() {
        JFrame frame = new JFrame("Monster Mayhem");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().add(this);
        frame.pack();
        frame.setVisible(true);
    }
    /**
     * This class represents the action listener for the button.
     */
    private class ButtonClickListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            // Update the label text when the button is clicked
            label.setText("Button Clicked");
        }
    }
    /**
     * This method is called when the panel needs to be painted.
     *
     * @param g The Graphics object used for painting.
     */
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        // Add your custom painting logic here
        g.setColor(Color.RED);
        g.fillRect(0, 0, getWidth(), getHeight());
    }
}