/**
 * This class represents the main application logic and GUI.
 * It creates the main window and handles user interactions.
 */
import javax.swing.*;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
public class Application implements UserActionListener {
    private JFrame mainWindow;
    private List<Game> games;
    public Application() {
        games = new ArrayList<>();
    }
    public void start() {
        // Create the main window
        mainWindow = new JFrame("Board Game Score Tracker");
        mainWindow.setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
        mainWindow.setSize(800, 600);
        // Add a WindowListener to handle window closing event
        mainWindow.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                int choice = JOptionPane.showConfirmDialog(mainWindow, "Are you sure you want to exit?", "Confirm Exit", JOptionPane.YES_NO_OPTION);
                if (choice == JOptionPane.YES_OPTION) {
                    mainWindow.dispose(); // Close the window
                    System.exit(0); // Terminate the application
                }
            }
        });
        // Add components to the main window
        JPanel mainPanel = new JPanel();
        mainWindow.getContentPane().add(mainPanel);
        // Display the main window
        mainWindow.setVisible(true);
        // Prompt the user for actions
        String[] options = {"Create Game", "Add Players to Game", "Record Scores", "View Leaderboard"};
        String selectedOption = (String) JOptionPane.showInputDialog(mainWindow, "Select an action:", "Action Selection", JOptionPane.QUESTION_MESSAGE, null, options, options[0]);
        while (selectedOption != null) {
            onUserAction(selectedOption.toLowerCase().replace(" ", ""));
            selectedOption = (String) JOptionPane.showInputDialog(mainWindow, "Select an action:", "Action Selection", JOptionPane.QUESTION_MESSAGE, null, options, options[0]);
        }
    }
    @Override
    public void onUserAction(String action) {
        switch (action) {
            case "creategame":
                createGame();
                break;
            case "addplayerstogame":
                addPlayersToGame();
                break;
            case "recordscores":
                recordScores();
                break;
            case "viewleaderboard":
                viewLeaderboard();
                break;
            default:
                // Handle unknown action
                JOptionPane.showMessageDialog(mainWindow, "Unknown action: " + action);
                break;
        }
    }
    private void createGame() {
        String gameName = JOptionPane.showInputDialog(mainWindow, "Enter the game name:");
        String scoringRules = JOptionPane.showInputDialog(mainWindow, "Enter the scoring rules:");
        Game game = new Game(gameName, scoringRules);
        games.add(game);
        JOptionPane.showMessageDialog(mainWindow, "Game created successfully!");
    }
    private void addPlayersToGame() {
        if (games.isEmpty()) {
            JOptionPane.showMessageDialog(mainWindow, "No games available. Please create a game first.");
            return;
        }
        Game selectedGame = selectGame();
        if (selectedGame != null) {
            String playerName = JOptionPane.showInputDialog(mainWindow, "Enter the player name:");
            selectedGame.addPlayer(playerName);
            JOptionPane.showMessageDialog(mainWindow, "Player added successfully!");
        }
    }
    private void recordScores() {
        if (games.isEmpty()) {
            JOptionPane.showMessageDialog(mainWindow, "No games available. Please create a game first.");
            return;
        }
        Game selectedGame = selectGame();
        if (selectedGame != null) {
            String playerName = JOptionPane.showInputDialog(mainWindow, "Enter the player name:");
            int score = Integer.parseInt(JOptionPane.showInputDialog(mainWindow, "Enter the score:"));
            selectedGame.recordScore(playerName, score);
            JOptionPane.showMessageDialog(mainWindow, "Score recorded successfully!");
        }
    }
    private void viewLeaderboard() {
        if (games.isEmpty()) {
            JOptionPane.showMessageDialog(mainWindow, "No games available. Please create a game first.");
            return;
        }
        Game selectedGame = selectGame();
        if (selectedGame != null) {
            List<Player> players = selectedGame.getPlayers();
            Collections.sort(players, Comparator.comparingInt(Player::getScore).reversed());
            StringBuilder leaderboard = new StringBuilder();
            leaderboard.append("Leaderboard for ").append(selectedGame.getName()).append(":\n");
            for (Player player : players) {
                leaderboard.append(player.getName()).append(": ").append(player.getScore()).append("\n");
            }
            JOptionPane.showMessageDialog(mainWindow, leaderboard.toString());
        }
    }
    private Game selectGame() {
        String[] gameNames = new String[games.size()];
        for (int i = 0; i < games.size(); i++) {
            gameNames[i] = games.get(i).getName();
        }
        String selectedGameName = (String) JOptionPane.showInputDialog(mainWindow, "Select a game:", "Game Selection", JOptionPane.QUESTION_MESSAGE, null, gameNames, gameNames[0]);
        if (selectedGameName != null) {
            for (Game game : games) {
                if (game.getName().equals(selectedGameName)) {
                    return game;
                }
            }
        }
        return null;
    }
}