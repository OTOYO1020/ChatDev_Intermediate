import java.util.ArrayList;
import java.util.List;
import java.util.Random;
/**
 * This class represents the game logic and manages the game state.
 */
public class Game {
    private List<Player> players;
    private Arena arena;
    private boolean isRunning;
    public Game() {
        players = new ArrayList<>();
        arena = new Arena();
        isRunning = false;
    }
    public void start() {
        initializePlayers();
        isRunning = true;
        while (isRunning) {
            update();
            render();
        }
    }
    private void initializePlayers() {
        CharacterSelection characterSelection = new CharacterSelection();
        int numberOfPlayers = 2; // Change this value to the desired number of players
        for (int i = 0; i < numberOfPlayers; i++) {
            Character selectedCharacter = characterSelection.selectCharacter();
            Player player = new Player("Player " + (i + 1), selectedCharacter);
            players.add(player);
        }
    }
    private void update() {
        // Update player positions, check for collisions, handle spellcasting, etc.
        for (Player player : players) {
            player.updatePosition();
            if (!arena.isInside(player)) {
                player.takeDamage(arena.getShrinkRate());
            }
            player.castSpell();
        }
    }
    private void render() {
        // Display player information, arena boundaries, etc.
        clearScreen();
        for (Player player : players) {
            displayPlayerInfo(player);
        }
        displayArenaBoundaries();
    }
    public void endGame() {
        isRunning = false;
        // TODO: Implement end game logic
        // Determine the winner, display end game message, etc.
        System.out.println("Game Over");
    }
    private void clearScreen() {
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }
    private void displayPlayerInfo(Player player) {
        System.out.println("Player: " + player.getName());
        System.out.println("Health: " + player.getHealth());
        System.out.println("Character: " + player.getCharacter().getName());
        System.out.println();
    }
    private void displayArenaBoundaries() {
        System.out.println("Arena Boundaries:");
        System.out.println("Width: " + arena.getWidth());
        System.out.println("Height: " + arena.getHeight());
        System.out.println();
    }
}