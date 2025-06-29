/**
 * This class represents a position on the grid.
 */
public class GridPosition {
    private int row;
    private int column;
    public GridPosition(int row, int column) {
        this.row = row;
        this.column = column;
    }
    // Add necessary getter and setter methods for the fields
    public int getRow() {
        return row;
    }
    public void setRow(int row) {
        this.row = row;
    }
    public int getColumn() {
        return column;
    }
    public void setColumn(int column) {
        this.column = column;
    }
}