'''
This class handles the user input and controls the flow of the application.
'''
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import javax.swing.JOptionPane;
import gui.GUI;
public class Controller {
    private static GUI gui; // Add a static reference to the GUI instance
    public static void handleInput(String input) {
        // Validate input and perform necessary actions
        if (input != null && !input.isEmpty()) {
            String[] inputParts = input.split(",");
            if (inputParts.length != 2) {
                gui.showMessage("Invalid input. Please enter the number of players and player names separated by commas.");
                return;
            }
            String numPlayersStr = inputParts[0].trim();
            String[] playerNames = inputParts[1].split("\\s*,\\s*");
            int numPlayers;
            try {
                numPlayers = Integer.parseInt(numPlayersStr);
            } catch (NumberFormatException e) {
                gui.showMessage("Invalid input. Please enter a valid number of players.");
                return;
            }
            if (numPlayers != playerNames.length) {
                gui.showMessage("Invalid input. The number of players does not match the number of player names.");
                return;
            }
            String[] turnOrder = generateRandomTurnOrder(playerNames);
            gui.displayTurnOrder("Turn Order: " + String.join(", ", turnOrder));
        }
    }
    private static String[] generateRandomTurnOrder(String[] playerNames) {
        List<String> turnOrderList = Arrays.asList(playerNames);
        Collections.shuffle(turnOrderList);
        return turnOrderList.toArray(new String[0]);
    }
    public static void setGUI(GUI guiInstance) {
        gui = guiInstance; // Set the GUI instance
    }
}