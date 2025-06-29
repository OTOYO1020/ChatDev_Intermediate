/**
 * This class represents the main entry point of the Battle Squad game.
 */
public class Main {
    public static void main(String[] args) {
        // TODO: Implement the main logic of the game
        System.out.println("Welcome to Battle Squad!");
        // Add your game logic here
        // Create game objects
        Team playerTeam = new Team();
        Team enemyTeam = new Team();
        // Assemble player team
        Warrior warrior1 = new Warrior("Warrior 1");
        Warrior warrior2 = new Warrior("Warrior 2");
        Warrior warrior3 = new Warrior("Warrior 3");
        playerTeam.addWarrior(warrior1);
        playerTeam.addWarrior(warrior2);
        playerTeam.addWarrior(warrior3);
        // Assemble enemy team
        Warrior enemyWarrior1 = new Warrior("Enemy Warrior 1");
        Warrior enemyWarrior2 = new Warrior("Enemy Warrior 2");
        Warrior enemyWarrior3 = new Warrior("Enemy Warrior 3");
        enemyTeam.addWarrior(enemyWarrior1);
        enemyTeam.addWarrior(enemyWarrior2);
        enemyTeam.addWarrior(enemyWarrior3);
        // Start battle
        Battle battle = new Battle(playerTeam, enemyTeam);
        battle.start();
        // Create and display the GUI
        GUI gui = new GUI();
    }
}