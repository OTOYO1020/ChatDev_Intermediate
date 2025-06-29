'''
This file contains the Arena class that represents a battle arena in the game.
'''
public class Arena {
    private String name;
    private int width;
    private int height;
    public Arena(String name, int width, int height) {
        this.name = name;
        this.width = width;
        this.height = height;
    }
    public String getName() {
        return name;
    }
    public int getWidth() {
        return width;
    }
    public int getHeight() {
        return height;
    }
}