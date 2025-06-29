import java.util.Random;
public class DiceTower {
    private int diceValue;
    public void rollDice() {
        Random random = new Random();
        diceValue = random.nextInt(6) + 1;
    }
    public int getDiceValue() {
        return diceValue;
    }
}