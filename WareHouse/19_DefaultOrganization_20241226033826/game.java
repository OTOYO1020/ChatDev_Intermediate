'''
This file contains the Game class that manages the game logic and flow.
'''
public class Game {
    private Character player1;
    private Character player2;
    private Arena arena;
    public Game(Character player1, Character player2, Arena arena) {
        this.player1 = player1;
        this.player2 = player2;
        this.arena = arena;
    }
    public void start() {
        System.out.println("Game started!");
        System.out.println("Player 1: " + player1.getName());
        System.out.println("Player 2: " + player2.getName());
        System.out.println("Arena: " + arena.getName());
        System.out.println("Let the battle begin!");
        while (player1.getHealth() > 0 && player2.getHealth() > 0) {
            player1.attack(player2);
            player2.attack(player1);
        }
        if (player1.getHealth() > 0) {
            System.out.println(player1.getName() + " wins!");
        } else if (player2.getHealth() > 0) {
            System.out.println(player2.getName() + " wins!");
        } else {
            System.out.println("It's a draw!");
        }
        System.out.println("Game over!");
    }
    public void attack(Character attacker, Character target) {
        int damage = attacker.getAttack() - target.getDefense();
        if (damage > 0) {
            target.takeDamage(damage);
        }
        System.out.println(attacker.getName() + " attacks " + target.getName());
        System.out.println(target.getName() + " health: " + target.getHealth());
    }
}