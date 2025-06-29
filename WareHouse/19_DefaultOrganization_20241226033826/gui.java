'''
This file contains the GUI class that creates and manages the graphical user interface.
'''
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class GUI {
    private JFrame frame;
    private JButton button;
    private JLabel label;
    /**
     * Creates and shows the graphical user interface.
     */
    public void createAndShowGUI() {
        // Create the main frame
        frame = new JFrame("Arena Clash");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(800, 600);
        // Create the button
        button = new JButton("Click Me");
        button.addActionListener(new ButtonClickListener());
        // Create the label
        label = new JLabel("Hello World!");
        // Add components to the frame
        frame.getContentPane().setLayout(new FlowLayout());
        frame.getContentPane().add(button);
        frame.getContentPane().add(label);
        // Show the frame
        frame.setVisible(true);
    }
    private class ButtonClickListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent event) {
            label.setText("Button Clicked");
        }
    }
}