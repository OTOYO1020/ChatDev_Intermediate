import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.List;
/**
 * This class represents the graphical user interface of the application.
 * It creates the main window and handles user interactions.
 */
public class GUI {
    private JFrame frame;
    private JButton button;
    private JTextField playersField;
    private JTextField durationField;
    private JTextField complexityField;
    private JTextField themesField;
    private JTextArea recommendationsArea;
    private RecommendationEngine recommendationEngine;
    public void start() {
        frame = new JFrame("Application");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);
        frame.setLayout(new FlowLayout());
        JLabel playersLabel = new JLabel("Number of Players:");
        playersField = new JTextField(10);
        frame.add(playersLabel);
        frame.add(playersField);
        JLabel durationLabel = new JLabel("Game Duration:");
        durationField = new JTextField(10);
        frame.add(durationLabel);
        frame.add(durationField);
        JLabel complexityLabel = new JLabel("Game Complexity:");
        complexityField = new JTextField(10);
        frame.add(complexityLabel);
        frame.add(complexityField);
        JLabel themesLabel = new JLabel("Game Themes:");
        themesField = new JTextField(10);
        frame.add(themesLabel);
        frame.add(themesField);
        button = new JButton("Generate Recommendations");
        button.addActionListener(new ButtonClickListener());
        frame.add(button);
        recommendationsArea = new JTextArea(10, 30);
        recommendationsArea.setEditable(false);
        JScrollPane scrollPane = new JScrollPane(recommendationsArea);
        frame.add(scrollPane);
        recommendationEngine = new RecommendationEngine();
        frame.setVisible(true);
    }
    private class ButtonClickListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            int players = Integer.parseInt(playersField.getText());
            int duration = Integer.parseInt(durationField.getText());
            int complexity = Integer.parseInt(complexityField.getText());
            String themes = themesField.getText();
            List<BoardGame> recommendations = recommendationEngine.generateRecommendations(players, duration, complexity, themes);
            recommendationsArea.setText("");
            for (BoardGame game : recommendations) {
                recommendationsArea.append(game.toString() + "\n");
            }
        }
    }
}
/**
 * This class represents a board game with attributes such as number of players, game duration, complexity, and game themes.
 */
class BoardGame {
    private int players;
    private int duration;
    private int complexity;
    private String themes;
    public BoardGame(int players, int duration, int complexity, String themes) {
        this.players = players;
        this.duration = duration;
        this.complexity = complexity;
        this.themes = themes;
    }
    public int getPlayers() {
        return players;
    }
    public int getDuration() {
        return duration;
    }
    public int getComplexity() {
        return complexity;
    }
    public String getThemes() {
        return themes;
    }
    @Override
    public String toString() {
        return "BoardGame{" +
                "players=" + players +
                ", duration=" + duration +
                ", complexity=" + complexity +
                ", themes='" + themes + '\'' +
                '}';
    }
}
/**
 * This class represents the recommendation engine that handles the logic for generating personalized recommendations based on user preferences.
 */
class RecommendationEngine {
    private List<BoardGame> boardGames;
    public RecommendationEngine() {
        // Initialize the list of board games
        boardGames = new ArrayList<>();
        boardGames.add(new BoardGame(2, 30, 3, "Fantasy"));
        boardGames.add(new BoardGame(4, 60, 4, "Sci-Fi"));
        boardGames.add(new BoardGame(2, 45, 2, "Mystery"));
        boardGames.add(new BoardGame(3, 90, 5, "Adventure"));
        boardGames.add(new BoardGame(4, 120, 4, "Strategy"));
    }
    public List<BoardGame> generateRecommendations(int players, int duration, int complexity, String themes) {
        List<BoardGame> recommendations = new ArrayList<>();
        for (BoardGame game : boardGames) {
            if (game.getPlayers() >= players &&
                    game.getDuration() <= duration &&
                    game.getComplexity() <= complexity &&
                    game.getThemes().contains(themes)) {
                recommendations.add(game);
            }
        }
        return recommendations;
    }
}