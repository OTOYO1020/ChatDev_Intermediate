import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;
/**
 * This class represents the graphical user interface for the board game rule generator application.
 */
public class GUI extends JFrame {
    private JButton generateButton;
    private JLabel ruleLabel;
    private JComboBox<String> categoryComboBox;
    private JSlider difficultySlider;
    private JTextArea ruleTextArea;
    private JButton saveButton;
    private JButton shareButton;
    /**
     * Constructor to initialize the GUI components and set up the layout.
     */
    public GUI() {
        // Set the title of the window
        super("Board Game Rule Generator");
        // Set the size of the window
        setSize(400, 300);
        // Set the default close operation
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Create the main panel
        JPanel mainPanel = new JPanel();
        mainPanel.setLayout(new BorderLayout());
        // Create the rule panel
        JPanel rulePanel = new JPanel();
        rulePanel.setLayout(new BorderLayout());
        // Create the rule label
        ruleLabel = new JLabel("Generated Rule:");
        rulePanel.add(ruleLabel, BorderLayout.NORTH);
        // Create the rule text area
        ruleTextArea = new JTextArea();
        ruleTextArea.setEditable(false);
        rulePanel.add(new JScrollPane(ruleTextArea), BorderLayout.CENTER);
        // Create the category panel
        JPanel categoryPanel = new JPanel();
        categoryPanel.setLayout(new FlowLayout());
        // Create the category label
        JLabel categoryLabel = new JLabel("Category:");
        categoryPanel.add(categoryLabel);
        // Create the category combo box
        categoryComboBox = new JComboBox<>();
        categoryComboBox.addItem("Movement");
        categoryComboBox.addItem("Scoring");
        categoryComboBox.addItem("Special Abilities");
        categoryComboBox.addItem("Win Conditions");
        categoryPanel.add(categoryComboBox);
        // Create the difficulty panel
        JPanel difficultyPanel = new JPanel();
        difficultyPanel.setLayout(new FlowLayout());
        // Create the difficulty label
        JLabel difficultyLabel = new JLabel("Difficulty:");
        difficultyPanel.add(difficultyLabel);
        // Create the difficulty slider
        difficultySlider = new JSlider(1, 10);
        difficultySlider.setMajorTickSpacing(1);
        difficultySlider.setPaintTicks(true);
        difficultySlider.setPaintLabels(true);
        difficultyPanel.add(difficultySlider);
        // Create the generate button
        generateButton = new JButton("Generate Rule");
        generateButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                generateRule();
            }
        });
        // Create the save button
        saveButton = new JButton("Save Rule");
        // Create the share button
        shareButton = new JButton("Share Rule");
        // Create the button panel
        JPanel buttonPanel = new JPanel();
        buttonPanel.setLayout(new FlowLayout());
        buttonPanel.add(generateButton);
        buttonPanel.add(saveButton);
        buttonPanel.add(shareButton);
        // Add the panels to the main panel
        mainPanel.add(rulePanel, BorderLayout.CENTER);
        mainPanel.add(categoryPanel, BorderLayout.NORTH);
        mainPanel.add(difficultyPanel, BorderLayout.SOUTH);
        mainPanel.add(buttonPanel, BorderLayout.EAST);
        // Add the main panel to the frame
        add(mainPanel);
    }
    /**
     * Method to start the application and make the GUI visible.
     */
    public void start() {
        setVisible(true);
    }
    /**
     * Method to generate a random rule based on the selected category and difficulty level.
     */
    private void generateRule() {
        String category = (String) categoryComboBox.getSelectedItem();
        if (category != null) {
            int difficulty = difficultySlider.getValue();
            // Generate a random rule based on the selected category and difficulty level
            String rule = generateRandomRule(category, difficulty);
            // Update the rule text area with the generated rule
            ruleTextArea.setText(rule);
        } else {
            // Display an error message dialog
            JOptionPane.showMessageDialog(this, "Please select a category", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }
    /**
     * Method to generate a random rule based on the selected category and difficulty level.
     *
     * @param category   The selected category.
     * @param difficulty The selected difficulty level.
     * @return A randomly generated rule.
     */
    private String generateRandomRule(String category, int difficulty) {
        Random random = new Random();
        String rule = "";
        switch (category) {
            case "Movement":
                rule = generateMovementRule(difficulty, random);
                break;
            case "Scoring":
                rule = generateScoringRule(difficulty, random);
                break;
            case "Special Abilities":
                rule = generateSpecialAbilitiesRule(difficulty, random);
                break;
            case "Win Conditions":
                rule = generateWinConditionsRule(difficulty, random);
                break;
            default:
                rule = "Invalid category";
                break;
        }
        return rule;
    }
    /**
     * Method to generate a random movement rule based on the selected difficulty level.
     *
     * @param difficulty The selected difficulty level.
     * @param random     The random number generator.
     * @return A randomly generated movement rule.
     */
    private String generateMovementRule(int difficulty, Random random) {
        // Implement the logic to generate a random movement rule based on the selected difficulty level
        String[] movementRules = {
                "Move forward 3 spaces",
                "Move backward 2 spaces",
                "Skip the next turn",
                "Swap positions with another player",
                "Move to a random location on the board"
        };
        int index = random.nextInt(movementRules.length);
        return movementRules[index];
    }
    /**
     * Method to generate a random scoring rule based on the selected difficulty level.
     *
     * @param difficulty The selected difficulty level.
     * @param random     The random number generator.
     * @return A randomly generated scoring rule.
     */
    private String generateScoringRule(int difficulty, Random random) {
        // Implement the logic to generate a random scoring rule based on the selected difficulty level
        String[] scoringRules = {
                "Score 10 points for each captured piece",
                "Double the score for the next move",
                "Score 5 points for each piece on the opponent's side",
                "Score 1 point for each space moved",
                "Score 20 points for reaching the opponent's base"
        };
        int index = random.nextInt(scoringRules.length);
        return scoringRules[index];
    }
    /**
     * Method to generate a random special abilities rule based on the selected difficulty level.
     *
     * @param difficulty The selected difficulty level.
     * @param random     The random number generator.
     * @return A randomly generated special abilities rule.
     */
    private String generateSpecialAbilitiesRule(int difficulty, Random random) {
        // Implement the logic to generate a random special abilities rule based on the selected difficulty level
        String[] specialAbilitiesRules = {
                "Steal a card from another player",
                "Skip the next penalty",
                "Swap hands with another player",
                "Draw 2 extra cards",
                "Reverse the direction of play"
        };
        int index = random.nextInt(specialAbilitiesRules.length);
        return specialAbilitiesRules[index];
    }
    /**
     * Method to generate a random win conditions rule based on the selected difficulty level.
     *
     * @param difficulty The selected difficulty level.
     * @param random     The random number generator.
     * @return A randomly generated win conditions rule.
     */
    private String generateWinConditionsRule(int difficulty, Random random) {
        // Implement the logic to generate a random win conditions rule based on the selected difficulty level
        String[] winConditionsRules = {
                "Be the first player to reach 100 points",
                "Capture all of the opponent's pieces",
                "Control all the territories on the board",
                "Survive until the end of the game",
                "Complete a specific objective card"
        };
        int index = random.nextInt(winConditionsRules.length);
        return winConditionsRules[index];
    }
}