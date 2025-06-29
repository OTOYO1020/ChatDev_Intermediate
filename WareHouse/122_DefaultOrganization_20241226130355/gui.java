'''
This class represents the GUI for displaying the curated collection of literature, music, visual arts, and films.
'''
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class GUI extends JFrame {
    private JButton literatureButton;
    private JButton musicButton;
    private JButton visualArtsButton;
    private JButton filmsButton;
    private JTextArea displayArea;
    private DataLoader dataLoader; // Added DataLoader instance
    /**
     * Creates and displays the GUI.
     */
    public void createAndShowGUI() {
        setTitle("Cultural Exploration");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(800, 600);
        setLocationRelativeTo(null);
        // Create buttons
        literatureButton = new JButton("Literature");
        musicButton = new JButton("Music");
        visualArtsButton = new JButton("Visual Arts");
        filmsButton = new JButton("Films");
        // Create display area
        displayArea = new JTextArea();
        displayArea.setEditable(false);
        // Create button panel
        JPanel buttonPanel = new JPanel();
        buttonPanel.setLayout(new FlowLayout());
        buttonPanel.add(literatureButton);
        buttonPanel.add(musicButton);
        buttonPanel.add(visualArtsButton);
        buttonPanel.add(filmsButton);
        // Create main panel
        JPanel mainPanel = new JPanel();
        mainPanel.setLayout(new BorderLayout());
        mainPanel.add(buttonPanel, BorderLayout.NORTH);
        mainPanel.add(new JScrollPane(displayArea), BorderLayout.CENTER);
        // Add main panel to the JFrame
        getContentPane().add(mainPanel);
        // Create DataLoader instance
        dataLoader = new DataLoader();
        // Add action listeners to the buttons
        literatureButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                loadItems("literature");
            }
        });
        musicButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                loadItems("music");
            }
        });
        visualArtsButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                loadItems("visual arts");
            }
        });
        filmsButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                loadItems("films");
            }
        });
        setVisible(true);
    }
    /**
     * Loads items from the specified category.
     */
    private void loadItems(String category) {
        // Clear the display area before loading new items
        displayArea.setText("");
        displayArea.setText("Loading " + category + "...\n");
        displayArea.append(category + " from various cultures:\n");
        // Fetch items from the data source or database based on the category
        // using the DataLoader instance
        displayArea.append(String.join("\n", dataLoader.getItems(category)));
    }
}