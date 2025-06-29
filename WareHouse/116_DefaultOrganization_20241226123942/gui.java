import javax.swing.*;
import java.awt.*;
/**
 * This class represents the graphical user interface of the web application.
 */
public class GUI extends JFrame {
    private JButton inputButton;
    private JButton generateButton;
    private JButton visualizeButton;
    public GUI() {
        // Code to create and configure the GUI components
        // For example, you can create buttons, labels, and text fields
        inputButton = new JButton("Input Sales Data");
        generateButton = new JButton("Generate Reports");
        visualizeButton = new JButton("Visualize Sales Performance");
        // Configure the layout manager
        setLayout(new FlowLayout());
        // Add the components to the frame
        add(inputButton);
        add(generateButton);
        add(visualizeButton);
        // Configure the frame
        setTitle("Business Sales Performance Tracker");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
    }
    public JButton getInputButton() {
        return inputButton;
    }
    public JButton getGenerateButton() {
        return generateButton;
    }
    public JButton getVisualizeButton() {
        return visualizeButton;
    }
}