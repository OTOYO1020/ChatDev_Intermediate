import java.util.Scanner;
/**
 * This class represents the game logic for Ninja Duel.
 * It handles the turn-based gameplay and win conditions.
 */
public class Game {
    private Ninja player1;
    private Ninja player2;
    private Scanner scanner;
    public Game() {
        scanner = new Scanner(System.in);
    }
    public void start() {
        // Create player 1
        System.out.println("Enter player 1 name:");
        String player1Name = scanner.nextLine();
        player1 = createNinja(player1Name);
        // Create player 2
        System.out.println("Enter player 2 name:");
        String player2Name = scanner.nextLine();
        player2 = createNinja(player2Name);
        // Start the game
        System.out.println("Let the battle begin!");
        while (player1.isAlive() && player2.isAlive()) {
            playTurn(player1, player2);
            if (!player2.isAlive()) {
                break;
            }
            playTurn(player2, player1);
        }
        // Determine the winner
        if (player1.isAlive()) {
            System.out.println(player1.getName() + " wins!");
        } else if (player2.isAlive()) {
            System.out.println(player2.getName() + " wins!");
        } else {
            System.out.println("It's a draw!");
        }
    }
    private Ninja createNinja(String name) {
        System.out.println("Create a ninja: " + name);
        System.out.println("Enter health:");
        int health = scanner.nextInt();
        System.out.println("Enter attack power:");
        int attackPower = scanner.nextInt();
        System.out.println("Enter defense power:");
        int defensePower = scanner.nextInt();
        scanner.nextLine(); // Consume the newline character
        System.out.println("Enter special move:");
        String specialMove = scanner.nextLine();
        return new Ninja(name, health, attackPower, defensePower, specialMove);
    }
    private void playTurn(Ninja attacker, Ninja defender) {
        System.out.println(attacker.getName() + "'s turn");
        System.out.println("Choose an action:");
        System.out.println("1. Attack");
        System.out.println("2. Use special move");
        int choice = scanner.nextInt();
        scanner.nextLine(); // Consume the newline character
        switch (choice) {
            case 1:
                attacker.attack(defender);
                System.out.println(attacker.getName() + " attacks " + defender.getName());
                System.out.println(defender.getName() + " takes " + (attacker.getAttackPower() - defender.getDefensePower()) + " damage");
                break;
            case 2:
                System.out.println(attacker.getName() + " uses special move: " + attacker.getSpecialMove());
                break;
            default:
                System.out.println("Invalid choice");
                break;
        }
        System.out.println(attacker.getName() + "'s health: " + attacker.getHealth());
        System.out.println(defender.getName() + "'s health: " + defender.getHealth());
        System.out.println();
    }
}