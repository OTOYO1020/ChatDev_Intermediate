'''
This is the main file that serves as the entry point for the application.
'''
import javax.swing.*;
import GUI.GUI;
import character.Character;
import arena.Arena;
import game.Game;
public class Main {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            // Create and show the GUI
            GUI gui = new GUI();
            gui.createAndShowGUI();
            // Create characters
            Character player1 = new Character("Player 1", "Aggressive", 100, 20, 10);
            Character player2 = new Character("Player 2", "Defensive", 100, 15, 15);
            // Create arena
            Arena arena = new Arena("Arena 1", 800, 600);
            // Create game
            Game game = new Game(player1, player2, arena);
            // Start the game
            game.start();
        });
    }
}