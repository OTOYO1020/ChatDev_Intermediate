import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the graphical user interface of the program.
 */
public class GUI extends JFrame {
    private JButton button;
    private JLabel label;
    private JTextArea textArea;
    private GameAnalyzer gameAnalyzer;
    public GUI(GameAnalyzer gameAnalyzer) {
        this.gameAnalyzer = gameAnalyzer;
        // Set up the main frame
        setTitle("Board Game Analyzer");
        setSize(800, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());
        // Create the button
        button = new JButton("Analyze");
        // Create the label
        label = new JLabel("Click the button to analyze board game strategies.");
        // Create the text area
        textArea = new JTextArea();
        textArea.setEditable(false);
        // Create a scroll pane to add scroll functionality to the text area
        JScrollPane scrollPane = new JScrollPane(textArea);
        // Add the button, label, and scroll pane to the frame
        add(button, BorderLayout.NORTH);
        add(label, BorderLayout.CENTER);
        add(scrollPane, BorderLayout.SOUTH);
        // Add action listener to the button
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Call the analyze method of GameAnalyzer when the button is clicked
                gameAnalyzer.analyze();
            }
        });
    }
    /**
     * This method returns the text area.
     */
    public JTextArea getTextArea() {
        return textArea;
    }
}