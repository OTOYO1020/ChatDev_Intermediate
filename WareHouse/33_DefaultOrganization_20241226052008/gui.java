'''
This file contains the GUI class that creates and manages the graphical user interface of the application.
'''
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class GUI {
    private JFrame frame;
    private JButton button;
    private JLabel label;
    public void createAndShowGUI() {
        frame = new JFrame("Dice Roll Simulator");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new FlowLayout());
        button = new JButton("Roll Dice");
        button.addActionListener(new ButtonClickListener());
        label = new JLabel("Results will be displayed here.");
        frame.add(button);
        frame.add(label);
        frame.pack();
        frame.setVisible(true);
    }
    private class ButtonClickListener implements ActionListener {
        public void actionPerformed(ActionEvent event) {
            try {
                // Get the number and type of dice selected by the user
                String numberOfDiceInput = JOptionPane.showInputDialog(frame, "Enter the number of dice:");
                String diceTypeInput = JOptionPane.showInputDialog(frame, "Enter the type of dice (e.g. 6 for a standard six-sided dice):");
                // Check if the user canceled or closed the input dialog
                if (numberOfDiceInput == null || diceTypeInput == null) {
                    return;
                }
                // Validate the input
                if (!numberOfDiceInput.matches("-?\\d+") || !diceTypeInput.matches("-?\\d+")) {
                    JOptionPane.showMessageDialog(frame, "Invalid input. Please enter an integer value for the number of dice and dice type.");
                    return;
                }
                int numberOfDice;
                int diceType;
                try {
                    numberOfDice = Integer.parseInt(numberOfDiceInput);
                    diceType = Integer.parseInt(diceTypeInput);
                } catch (NumberFormatException e) {
                    JOptionPane.showMessageDialog(frame, "Invalid input. Please enter a valid integer value for the number of dice and dice type.");
                    return;
                }
                if (numberOfDice <= 0 || diceType <= 0) {
                    JOptionPane.showMessageDialog(frame, "Invalid input. Please enter a positive integer value for the number of dice and dice type.");
                    return;
                }
                // Roll the dice and display the results
                StringBuilder result = new StringBuilder();
                for (int i = 0; i < numberOfDice; i++) {
                    int roll = (int) (Math.random() * diceType) + 1;
                    result.append("Dice ").append(i + 1).append(": ").append(roll).append("\n");
                }
                label.setText(result.toString());
            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(frame, "Invalid input. Please enter a valid integer value for the number of dice and dice type.");
            }
        }
    }
}