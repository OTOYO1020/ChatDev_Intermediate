/**
 * This class represents a tile in the game.
 * Each tile has an ID and a color.
 */
public class Tile {
    private int id;
    private String color;
    public Tile(int id, String color) {
        this.id = id;
        this.color = color;
    }
    public int getId() {
        return id;
    }
    public String getColor() {
        return color;
    }
    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null || getClass() != obj.getClass()) {
            return false;
        }
        Tile other = (Tile) obj;
        return id == other.id && color.equals(other.color);
    }
    @Override
    public int hashCode() {
        return Objects.hash(id, color);
    }
}