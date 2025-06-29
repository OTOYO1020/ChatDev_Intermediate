/**
 * This class represents a player aid for games.
 */
public class PlayerAid {
    private String aidText;
    /**
     * Constructs a PlayerAid object with the specified aid text.
     *
     * @param aidText the text of the player aid
     */
    public PlayerAid(String aidText) {
        this.aidText = aidText;
    }
    /**
     * Displays the player aid.
     */
    public void displayAid() {
        System.out.println(aidText);
    }
}