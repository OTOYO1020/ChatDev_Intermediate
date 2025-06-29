/**
 * This class represents the game arena.
 */
public class Arena {
    private int width;
    private int height;
    private int shrinkRate;
    public Arena() {
        this.width = 1000;
        this.height = 1000;
        this.shrinkRate = 10;
    }
    public int getWidth() {
        return width;
    }
    public int getHeight() {
        return height;
    }
    public int getShrinkRate() {
        return shrinkRate;
    }
    public void shrink() {
        width -= shrinkRate;
        height -= shrinkRate;
    }
    public boolean isInside(Player player) {
        int playerX = player.getPosition().getX();
        int playerY = player.getPosition().getY();
        return playerX >= 0 && playerX <= width && playerY >= 0 && playerY <= height;
    }
}