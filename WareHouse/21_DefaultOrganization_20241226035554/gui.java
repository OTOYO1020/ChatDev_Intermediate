import javax.swing.JFrame;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JComboBox;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the GUI for the Superhero Showdown game.
 */
public class GUI {
    private JFrame frame;
    /**
     * Constructor for the GUI class.
     */
    public GUI() {
        // Initialize the main window
        frame = new JFrame("Superhero Showdown");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new FlowLayout());
        // Add components to the main window
        JButton button = new JButton("Start Game");
        frame.add(button);
        JLabel label = new JLabel("Select a superhero:");
        frame.add(label);
        String[] superheroes = {"Superman", "Batman", "Spider-Man"};
        JComboBox<String> comboBox = new JComboBox<>(superheroes);
        frame.add(comboBox);
        // Add action listener for the button
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Perform actions when the button is clicked
                String selectedSuperhero = (String) comboBox.getSelectedItem();
                System.out.println("Selected superhero: " + selectedSuperhero);
            }
        });
        // Set the size of the main window
        frame.setSize(400, 200);
    }
    /**
     * This method makes the main window visible.
     */
    public void start() {
        // Make the main window visible
        frame.setVisible(true);
    }
}